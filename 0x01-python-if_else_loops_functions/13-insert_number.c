#include "lists.h"

/**
* *insert_node - inserts a number in listint_t
*
* @head: pointer to pointer to head
*
* @number: number to be inserted
*
* Return: address of new node or
* NULL if it fails
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current != NULL && current->next->n < number)
		{
			current = current->next;
		}

		new_node->next = current->next;
		current->next = new_node;
	}

	return (new_node);
}
