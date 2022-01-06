#include "palindrome.h"

/**
 * is_palindrome - check if an unisnged int is a palindrome
 * @n: unsigned long int to check
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(unsigned long n)
{
	unsigned long rev = 0, tmp = n;

	while (tmp)
	{
		rev = rev * 10 + tmp % 10;
		tmp /= 10;
	}
	if (n == rev)
		return (1);
	return (0);
}
