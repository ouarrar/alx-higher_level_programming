#include "lists.h"

/**
 * check_cycle - Checks if a linked list contains a cycle.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't.
 */
int check_cycle(listint_t *head)
{
	listint_t *slow_ptr = head;
	listint_t *fast_ptr = head;

	if (!head)
	{
		return (0);
	}

	while (slow_ptr && fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
		{
			return (1);
		}
	}

	return (0);
}

