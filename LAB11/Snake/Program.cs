using System;
using System.Collections.Generic;

Exception? exception = null;
int speedInput;
string prompt = $"Select speed [1], [2] (default), or [3]: ";
string? input;
Console.Write(prompt);
while (!int.TryParse(input = Console.ReadLine(), out speedInput) || speedInput < 1 || 3 < speedInput)
{
	if (string.IsNullOrWhiteSpace(input))
	{
		speedInput = 2;
		break;
	}
	else
	{
		Console.WriteLine("Invalid Input. Try Again...");
		Console.Write(prompt);
	}
}
int[] velocities = [100, 70, 50];
int velocity = velocities[speedInput - 1];
char[] DirectionChars = ['^', 'v', '<', '>',];
TimeSpan sleep = TimeSpan.FromMilliseconds(velocity);
int width = Console.WindowWidth;
int height = Console.WindowHeight;
Tile[,] map = new Tile[width, height];
Direction? direction = null;
Queue<(int X, int Y)> snake = new();
(int X, int Y) = (width / 2, height / 2);
bool closeRequested = false;

try
{
	Console.CursorVisible = false;
	Console.Clear();
	snake.Enqueue((X, Y));
	map[X, Y] = Tile.Snake;
	PositionFood();
	Console.SetCursorPosition(X, Y);
	Console.Write('@');
	// Wait for user input before starting movement
	while (!direction.HasValue && !closeRequested)
	{
		GetDirection();
	}

	// Ensure direction is set before movement begins
	if (!direction.HasValue)
	{
		direction = Direction.Right; // Default start direction
	}

	while (!closeRequested)
	{
		if (Console.WindowWidth != width || Console.WindowHeight != height)
		{
			Console.Clear();
			Console.Write("Console was resized. Snake game has ended.");
			return;
		}
		switch (direction)
		{
			case Direction.Up: Y--; break;
			case Direction.Down: Y++; break;
			case Direction.Left: X--; break;
			case Direction.Right: X++; break;
		}
		if (X < 0 || X >= width ||
			Y < 0 || Y >= height ||
			map[X, Y] is Tile.Snake)
		{
			Console.WriteLine("Game Over. Score: " + (snake.Count - 1) + ".");
			System.Threading.Thread.Sleep(3000); // Pause before clearing
			Console.Clear();

		}
		Console.SetCursorPosition(X, Y);
		Console.Write(DirectionChars[(int)direction!]);
		snake.Enqueue((X, Y));
		if (map[X, Y] is Tile.Food)
		{
			PositionFood();
		}
		else
		{
			(int x, int y) = snake.Dequeue();
			map[x, y] = Tile.Open;
			Console.SetCursorPosition(x, y);
			Console.Write(' ');
		}
		map[X, Y] = Tile.Snake;
		if (Console.KeyAvailable)
		{
			GetDirection();
		}
		System.Threading.Thread.Sleep(sleep);
	}
}
catch (Exception e)
{
	exception = e;
	throw;
}
finally
{
	Console.CursorVisible = true;
	Console.Clear();
	Console.WriteLine(exception?.ToString() ?? "Snake was closed.");
}
void GetDirection()
{
	ConsoleKey key = Console.ReadKey(true).Key;

	// Ensure direction is set before checking constraints
	if (direction == null)
	{
		direction = key switch
		{
			ConsoleKey.UpArrow => Direction.Up,
			ConsoleKey.DownArrow => Direction.Down,
			ConsoleKey.LeftArrow => Direction.Left,
			ConsoleKey.RightArrow => Direction.Right,
			_ => direction
		};
		return;
	}

	// Prevent reversing direction
	if ((key == ConsoleKey.UpArrow && direction != Direction.Down) ||
		(key == ConsoleKey.DownArrow && direction != Direction.Up) ||
		(key == ConsoleKey.LeftArrow && direction != Direction.Right) ||
		(key == ConsoleKey.RightArrow && direction != Direction.Left))
	{
		direction = key switch
		{
			ConsoleKey.UpArrow => Direction.Up,
			ConsoleKey.DownArrow => Direction.Down,
			ConsoleKey.LeftArrow => Direction.Left,
			ConsoleKey.RightArrow => Direction.Right,
			_ => direction
		};
	}
}



void PositionFood()
{
	List<(int X, int Y)> possibleCoordinates = new();
	for (int i = 0; i < width; i++)
	{
		for (int j = 0; j < height; j++)
		{
			if (map[i, j] is Tile.Open)
			{
				possibleCoordinates.Add((i, j));
			}
		}
	}

	if (possibleCoordinates.Count > 0) // Fix: Avoids crash when no space is left
	{
		int index = Random.Shared.Next(possibleCoordinates.Count);
		(int X, int Y) = possibleCoordinates[index];
		map[X, Y] = Tile.Food;
		Console.SetCursorPosition(X, Y);
		Console.Write('+');
	}
}


enum Direction
{
	Up = 0,
	Down = 1,
	Left = 2,
	Right = 3,
}

enum Tile
{
	Open = 0,
	Snake,
	Food,
}
