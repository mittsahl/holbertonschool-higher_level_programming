#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a at proper position in sorted length
 * Return: pointer to new node
 * @head: head of linked list
 * @number: number for new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *previous = NULL, *h = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	for (; h->n <= new->n; previous = h, h = h->next)
		;
	previous->next = new;
	new->next = h;
	return (new);
}
