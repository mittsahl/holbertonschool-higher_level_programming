#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checsk to see if there is a loop inside the linked list
 * Return: 1 if loop else 0
 * @t: head of linked list
 */
int check_cycle(listint_t *t)
{
	listint_t *slow, *fast;

	if (t->next == t || t == NULL || t->next == NULL)
		return (1);
	slow = t;
	fast = t->next;
	while (fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
