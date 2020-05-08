#include "lists.h"
#include <stdlib.h>

/**
 * reverse - function to reverse the linked list note that this
 * function may change the head
 * @head: the head node of the linked list
 * Return: pointer to the new head
 */
listint_t *reverse(listint_t **head)
{
	listint_t *current;
	listint_t *aux;

	current = *head;
	if (current == NULL)
		return (NULL);

	while (current->next != NULL)
	{
		aux = current->next;
		current->next = aux->next;
		aux->next = *head;
		*head = aux;
	}
	return (*head);
}

/**
 * get_middle_node - function that gets the middle node
 * of a list
 * @head: the head node of the linked list
 * Return: pointer to the middle node
 */
listint_t *get_middle_node(listint_t **head)
{
	listint_t *slow_runner;
	listint_t *fast_runner;

	if (head == NULL)
		return (NULL);
	slow_runner = *head;
	fast_runner = *head;
	if (slow_runner->next == NULL)
		return (slow_runner);

	while (fast_runner && fast_runner->next)
	{
		slow_runner = slow_runner->next;
		fast_runner = fast_runner->next->next;
	}
	return (slow_runner);
}

/**
 * is_palindrome - function that checks if
 * the list is palindrome
 * @head:the head node of the linked list
 * Return: 0 if it is not a palindrome, 1 if
 * it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_part;
	listint_t *second_part;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	first_part = *head;
	second_part = get_middle_node(head);
	second_part = reverse(&second_part);
	while (second_part)
	{
		if (first_part->n != second_part->n)
			return (0);
		first_part = first_part->next;
		second_part = second_part->next;
	}
	return (1);
}
