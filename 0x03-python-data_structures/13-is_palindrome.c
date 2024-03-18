#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the linked list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (1);

	if ((*head)->next == NULL)
		return (1);

	listint_t *tort, *hare, *ptort;
	listint_t *cut = NULL, *half;

	tort = hare = *head;

	while (hare != NULL && hare->next != NULL)
	{
		ptort = tort;
		tort = tort->next;
		hare = hare->next->next;
	}

	if (hare != NULL)
	{
		cut = tort;
		tort = tort->next;
	}

	ptort->next = NULL;
	half = tort;

	if (!compare_lists(*head, reverse_listint(&half)))
	{
		reverse_listint(&half);
		restore_list(ptort, cut, half);
		return (0);
	}

	reverse_listint(&half);
	restore_list(ptort, cut, half);

	return (1);
}

/**
 * compare_lists - Compares two linked lists for equality
 * @list1: Pointer to the head of the first list
 * @list2: Pointer to the head of the second list
 *
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
	while (list1 && list2)
	{
		if (list1->n != list2->n)
		return (0);
		list1 = list1->next;
		list2 = list2->next;
	}

	return (1);
}

/**
 * reverse_listint - Reverses a linked list in place
 * @head: Pointer to a pointer pointing to the first item in the list
 *
 * Return: The new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL;

	if (!head || !*head)
		return (NULL);

	while ((*head)->next)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	(*head)->next = prev;

	return (*head);
}

/**
 * restore_list - Restores the original list after palindrome check
 * @ptort: Pointer to the node before the middle of the list
 * @cut: Pointer to the middle node (if list has odd number of nodes)
 * @half: Pointer to the second half of the list
 */
void restore_list(listint_t *ptort, listint_t *cut, listint_t *half)
{
	if (cut == NULL)
		ptort->next = half;
	else
	{
		ptort->next = cut;
		cut->next = half;
	}
}
