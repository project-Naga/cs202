using System;
using System.Timers;
using System.Threading.Tasks;

namespace AlarmAppConsole
{
    class Program
    {
        // Declare the delegate for the event  
        public delegate void AlarmEventHandler();

        // Define the event based on the delegate  
        public static event AlarmEventHandler raiseAlarm;

        // Target time to check against  
        static TimeSpan targetTime;
        static volatile bool isRunning = true;

        static async Task Main(string[] args)
        {
            Console.CancelKeyPress += (s, e) =>
            {
                isRunning = false;
                e.Cancel = true;
            };

            while (isRunning)
            {
                Console.WriteLine("Enter alarm time in HH:MM:SS format (or 'exit' to quit):");
                string input = Console.ReadLine();

                if (string.IsNullOrEmpty(input) || input.Equals("exit", StringComparison.OrdinalIgnoreCase))
                {
                    break;
                }

                if (TimeSpan.TryParse(input, out targetTime))
                {
                    if (targetTime < DateTime.Now.TimeOfDay)
                    {
                        Console.WriteLine("The entered time has already passed today.");
                        continue;
                    }

                    using var timer = new System.Timers.Timer(1000); // Fully qualify Timer to resolve ambiguity  
                    try
                    {
                        // Subscribe the Ring_alarm method to the event  
                        raiseAlarm += Ring_alarm;
                        timer.Elapsed += CheckTime;
                        timer.Start();

                        Console.WriteLine($"Alarm is set for {targetTime:hh\\:mm\\:ss}. Press Enter to cancel...");
                        await Task.Run(() => Console.ReadLine());

                        // Cleanup if user cancels  
                        timer.Stop();
                        raiseAlarm -= Ring_alarm;
                        Console.WriteLine("Alarm cancelled.");
                    }
                    catch (Exception ex)
                    {
                        Console.WriteLine($"Error: {ex.Message}");
                    }
                }
                else
                {
                    Console.WriteLine("Invalid time format. Please use HH:MM:SS format.");
                }
            }

            Console.WriteLine("Program terminated.");
        }

        private static void CheckTime(object sender, ElapsedEventArgs e)
        {
            if (!isRunning) return;

            TimeSpan currentTime = DateTime.Now.TimeOfDay;

            // Simplified time comparison with 1-second window  
            if (currentTime >= targetTime && currentTime < targetTime.Add(TimeSpan.FromSeconds(1)))
            {
                raiseAlarm?.Invoke();
                ((System.Timers.Timer)sender).Stop(); // Fully qualify Timer to resolve ambiguity  
                raiseAlarm -= Ring_alarm;
                Console.WriteLine("\nPress Enter to set another alarm or 'exit' to quit.");
            }
        }

        private static void Ring_alarm()
        {
            Console.Clear();
            for (int i = 0; i < 3; i++)
            {
                Console.WriteLine("⏰ ALARM TIME REACHED! RING RING! ⏰");
                Task.Delay(500).Wait();
                Console.Clear();
                Task.Delay(500).Wait();
            }
            Console.WriteLine("⏰ Alarm finished at: " + DateTime.Now.ToString("HH:mm:ss"));
        }
    }
}