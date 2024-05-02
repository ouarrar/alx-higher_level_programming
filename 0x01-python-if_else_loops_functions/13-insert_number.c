#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Inserts a node into a sorted linked list
 * @head: Pointer to the head of the list
 * @number: Value to insert into the list
 *
 * Return: A pointer to the newly inserted node or NULL on failure
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *current = *head;

	if (!new_node)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (current->next)
	{
		if ((current->next)->n >= number)
		{
			new_node->next = current->next;
			current->next = new_node;
			return (new_node);
		}
		current = current->next;
	}

	new_node->next = NULL;
	current->next = new_node;

	return (new_node);
}
