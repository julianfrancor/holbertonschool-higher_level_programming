#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function in C that inserts a number into
 * a sorted singly linked list.
 * @head: pointer to head of list
 * @number: number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prev;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;
	prev = NULL;
	current = *head;

	while (current && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	new->next = current;
	if (prev)
		prev->next = new;
	else
		*head = new;

	return (new);
}
