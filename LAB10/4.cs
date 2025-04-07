using System;

class Student
{
    public string Name { get; set; }
    public int ID { get; set; }
    public int Marks { get; set; }

    public Student(string name, int id, int marks)
    {
        Name = name;
        ID = id;
        Marks = marks;
    }

    public string GetGrade()
    {
        if (Marks >= 90) return "A";
        if (Marks >= 75) return "B";
        if (Marks >= 50) return "C";
        return "F";
    }

    public void Display()
    {
        Console.WriteLine($"Name: {Name}, ID: {ID}, Marks: {Marks}, Grade: {GetGrade()}");
    }
}

class StudentIITGN : Student
{
    public string Hostel_Name_IITGN { get; set; }

    public StudentIITGN(string name, int id, int marks, string hostel)
        : base(name, id, marks)
    {
        Hostel_Name_IITGN = hostel;
    }

    public new void Display()
    {
        base.Display();
        Console.WriteLine($"Hostel: {Hostel_Name_IITGN}");
    }
}

class Program
{
    static void Main()
    {
        StudentIITGN student = new StudentIITGN("Alice", 101, 85, "H1");
        student.Display();
    }
}
