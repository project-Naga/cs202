using System;

class Calculator
{
    static void Main()
    {
        Console.Write("Enter first number: ");
        int num1 = int.Parse(Console.ReadLine());

        Console.Write("Enter second number: ");
        int num2 = int.Parse(Console.ReadLine());

        int sum = num1 + num2;
        Console.WriteLine($"Addition: {sum}");
        Console.WriteLine($"Subtraction: {num1 - num2}");
        Console.WriteLine($"Multiplication: {num1 * num2}");
        Console.WriteLine($"Division: {(num2 != 0 ? (num1 / (double)num2).ToString() : "Cannot divide by zero")}");

        if (sum % 2 == 0)
            Console.WriteLine("Sum is even");
        else
            Console.WriteLine("Sum is odd");
    }
}
