using System;

class LoopDemo
{
    static int Factorial(int n)
    {
        int fact = 1;
        for (int i = 1; i <= n; i++)
        {
            fact *= i;
        }
        return fact;
    }

    static void Main()
    {
        for (int i = 1; i <= 10; i++)
        {
            Console.WriteLine(i);
        }

        string input;
        do
        {
            Console.Write("Enter a number (or 'exit' to quit): ");
            input = Console.ReadLine();

            if (input != "exit" && int.TryParse(input, out int num))
            {
                Console.WriteLine($"Factorial of {num} is {Factorial(num)}");
            }

        } while (input != "exit");
    }
}
