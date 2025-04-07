using System;

class SafeCalculator
{
    static void Main()
    {
        try
        {
            Console.Write("Enter first number: ");
            int num1 = int.Parse(Console.ReadLine());

            Console.Write("Enter second number: ");
            int num2 = int.Parse(Console.ReadLine());

            int sum = num1 + num2;
            Console.WriteLine($"Addition: {sum}");
            Console.WriteLine($"Subtraction: {num1 - num2}");
            Console.WriteLine($"Multiplication: {num1 * num2}");

            // Handle division separately
            if (num2 == 0)
            {
                Console.WriteLine("Error: Cannot divide by zero");
            }
            else
            {
                Console.WriteLine($"Division: {num1 / (double)num2}");
            }

            Console.WriteLine(sum % 2 == 0 ? "Sum is even" : "Sum is odd");
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input! Please enter numeric values only.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
