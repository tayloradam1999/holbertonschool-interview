#include "slide_line.h"

/**
 * slide_left - Slides the int on index i to the left
 * @line: Pointer to the array of int
 * @size: Number of elements in @line
 * @i: Index of the int to be moved
 */
void slide_left(int *line, size_t size, size_t i)
{
	size_t x;

	x = i + 1;
	while (x < size && !line[x])
		x++;
	if (x < size && line[x] != 0)
	{
		line[i] = line[x];
		line[x] = 0;
	}
}

/**
 * slide_right - Slides the int on index i to the right
 * @line: Pointer to the array of int
 * @i: Index of the int to be moved
 */
void slide_right(int *line, size_t i)
{
	int x;

	x = i - 1;
	while (x >= 0 && !line[x])
		x--;
	if (x >= 0 && line[x] != 0)
	{
		line[i] = line[x];
		line[x] = 0;
	}
}

/**
 * merge_left - merges to the left the int on index i and it's
 * identical neighbor on it's right side ONLY if they are contiguous or
 * seperated by zeros
 *
 * @line: Pointer to the array of int
 * @size: Number of elements in @line
 * @i: Index of the int to be moved
 */
void merge_left(int *line, size_t size, size_t i)
{
	size_t x;

	x = i + 1;
	if (x == size)
		return;
	while (x < size && line[x] == 0)
		x++;
	if (line[x] != line[i])
		return;
	line[i] *= 2;
	line[x] = 0;
}

/**
 * merge_right - merges to the right the int on index i and it's
 * identical neighbor on it's left side ONLY if they are contiguous or
 * seperated by zeros
 *
 * @line: Pointer to the array of int
 * @i: Index of the int to be moved
 */
void merge_right(int *line, int i)
{
	int x;

	x = i - 1;
	if (x < 0)
		return;
	while (x >= 0 && line[x] == 0)
		x--;
	if (x >= 0 && line[x] == line[i])
	{
		line[i] *= 2;
		line[x] = 0;
	}
}

/**
 * slide_line - Slides & merges an array of integers to the left or right
 * @line: Array of ints
 * @size: Size of @line
 * @direction: Direction to slide
 * Return: 1 if the array was slid, 0 otherwise
 */
int slide_line(int *line, size_t size, int direction)
{
	int x;

	if (!line || (direction != SLIDE_LEFT && direction != SLIDE_RIGHT))
		return (0);
	if (direction == SLIDE_LEFT)
	{
		for (x = 0; x < (int)size; x++)
		{
			if (line[x])
				merge_left(line, size, x);
		}
		for (x = 0; x < (int)size; x++)
		{
			if (line[x] == 0)
				slide_left(line, size, x);
		}
	}
	else if (direction == SLIDE_RIGHT)
	{
		for (x = (int)size - 1; x >= 0; x--)
		{
			if (line[x])
				merge_right(line, x);
		}
		for (x = (int)size - 1; x >= 0; x--)
		{
			if (line[x] == 0)
				slide_right(line, x);
		}
	}
	return (1);
}
