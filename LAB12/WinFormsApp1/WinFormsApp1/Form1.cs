using System;
using System.Drawing;
using System.Windows.Forms;

namespace AlarmAppWinForms
{
    public partial class Form1 : Form
    {
        public delegate void AlarmEventHandler();
        public event AlarmEventHandler raiseAlarm;

        private TimeSpan targetTime;
        private System.Windows.Forms.Timer timer; // Explicitly specify the namespace to resolve ambiguity  
        private Random rand;

        public Form1()
        {
            InitializeComponent();
            timer = new System.Windows.Forms.Timer(); // Explicitly specify the namespace to resolve ambiguity  
            timer.Interval = 1000; // 1 second  
            timer.Tick += CheckTime;
            rand = new Random();
        }

        private void btnStart_Click(object sender, EventArgs e)
        {
            if (TimeSpan.TryParse(txtTime.Text, out TimeSpan inputTime))
            {
                if (inputTime < DateTime.Now.TimeOfDay)
                {
                    MessageBox.Show("The entered time has already passed today.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                    return;
                }

                targetTime = inputTime;
                raiseAlarm += RingAlarm;
                timer.Start();
            }
            else
            {
                MessageBox.Show("Invalid time format. Use HH:MM:SS.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void CheckTime(object sender, EventArgs e)
        {
            TimeSpan current = DateTime.Now.TimeOfDay;

            // Change background color every tick  
            this.BackColor = Color.FromArgb(rand.Next(256), rand.Next(256), rand.Next(256));

            if (current >= targetTime && current < targetTime.Add(TimeSpan.FromSeconds(1)))
            {
                timer.Stop();
                raiseAlarm?.Invoke();
                raiseAlarm -= RingAlarm;
            }
        }

        private async void RingAlarm()
        {
            for (int i = 0; i < 3; i++)
            {
                this.BackColor = Color.Red;
                await Task.Delay(500);
                this.BackColor = Color.White;
                await Task.Delay(500);
            }

            MessageBox.Show("? Alarm time reached!", "Alarm", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
        }
    }
}
