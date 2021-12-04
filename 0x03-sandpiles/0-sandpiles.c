#include "sandpiles.h"

/**
 * print_grid - prints the grid
 * @grid: first sandpile
 * Return: void
 */
static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * check_stable - check if grid1 is stable
 * @grid1: First sandpile
 * Return: 1 if	stable, 0 if not
 */
int check_stable(int grid1[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid1[i][j] > 3)
				return (1);
		}
	}
	return (0);
}

/**
 * _topple - Handles toppling grid 1
 * @grid1: First sandpile
 * Return: void
 */
void _topple(int grid1[3][3])
{
	int i, j;

	int tmp_pile[3][3] = {
		{0, 0, 0},
		{0, 0, 0},
		{0, 0, 0}};

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
			tmp_pile[i][j] = grid1[i][j];
	}

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (grid1[i][j] > 3)
				grid1[i][j] -= 4;
			if ((i - 1) >= 0 && tmp_pile[i - 1][j] > 3)
				grid1[i][j]++;
			if ((i + 1) <= 2 && tmp_pile[i + 1][j] > 3)
				grid1[i][j]++;
			if ((j - 1) >= 0 && tmp_pile[i][j - 1] > 3)
				grid1[i][j]++;
			if ((j + 1) <= 2 && tmp_pile[i][j + 1] > 3)
				grid1[i][j]++;
		}
	}
}

/**
 * sandpiles_sum - Computes the sum of two sandpiles
 * @grid1: First sandpile
 * @grid2: Second sandpile
 * Return: void
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] += grid2[i][j];
		}
	}

	if (check_stable(grid1))
	{
		printf("=\n");
		print_grid(grid1);
	}

	while (check_stable(grid1))
	{
		_topple(grid1);
		if (check_stable(grid1))
		{
			printf("=\n");
			print_grid(grid1);
		}
	}
}
