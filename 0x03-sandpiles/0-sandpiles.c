#include "sandpiles.h"

/**
 * sandpiles_sum - Computes the sum of two sandpiles
 * @grid1: First sandpile
 * @grid2: Second sandpile
 * Return: void
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	/* You can assume both grid1 and grid2 are individually stable. */
	/* grid1 must be printed before each round of toppling. */
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] = grid1[i][j] + grid2[i][j];
		}
	}
	while (1)
	{
		if (grid1[0][0] > 3 || grid1[0][1] > 3 || grid1[0][2] > 3 ||
			grid1[1][0] > 3 || grid1[1][1] > 3 || grid1[1][2] > 3 ||
			grid1[2][0] > 3 || grid1[2][1] > 3 || grid1[2][2] > 3)
		{
			for (i = 0; i < 3; i++)
			{
				for (j = 0; j < 3; j++)
				{
					if (grid1[i][j] > 3)
					{
						grid1[i][j] = grid1[i][j] - 4;
						if (i > 0)
							grid1[i - 1][j]++;
						if (i < 2)
							grid1[i + 1][j]++;
						if (j > 0)
							grid1[i][j - 1]++;
						if (j < 2)
							grid1[i][j + 1]++;
					}
				}
			}
		}
		else
			break;
	}
}
