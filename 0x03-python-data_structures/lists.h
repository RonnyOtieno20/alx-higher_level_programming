#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

#include <stddef.h>

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
int is_palindrome(listint_t **head);
int compare_lists(listint_t *list1, listint_t *list2);
listint_t *reverse_listint(listint_t **head);
void restore_list(listint_t *ptort, listint_t *hcut, listint_t *half);
#endif /* LISTS_H */
