#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int i = 0, count = 0;
	listint_t *current, *front, *rear;

	if (head == NULL || *head == NULL)
	{
		print_listint(*head);
		return (1);
	}
	while (!*head)
	{
		count++;
		*head = (*head)->next;
	}
	while (i != count / 2)
	{
		current = *head;
		front = *head;
		rear = *head;
		while (current->next != NULL)
		{
			current = current->next;
			front = front->next;
			rear = rear->next->next;
		}
		if (front->n != rear->n)
			return (0);
		i++;
		*head = (*head)->next;
	}
	return (1);
}
