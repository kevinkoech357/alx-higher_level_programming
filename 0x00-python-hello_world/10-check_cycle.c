#include "lists.h"
#include <stddef.h>

/**
* check_cycle - checks if a linked list
* has a cycle
*
* @list: pointer to the list involved
*
* Return: 0 if there is no cycle
* or 1 if there's a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	first = second = list;

	if (list == NULL)
		return (0);

	while (first != NULL && first->next != NULL)
	{
		second = second->next;
		first = first->next->next;

		if (first == second)
			return (1);
	}

	return (0);
}

