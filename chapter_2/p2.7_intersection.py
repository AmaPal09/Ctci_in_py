#
# Intersection
# Given two (singly) linked lists, determine if the two lists intersect.
# Return the intersecting node. Note that the intersection is defined
# based on reference, not value. That is, if the kth node of the
# first linked list is the exact same node (by reference) as the jth
# node of the second linked list, then they are intersecting.
#  a->b->c->
# 			d->x->y->z
#  	  m->n->

#
# Explaination:
# If the 2 linked lists have intersecting nodes then the tails of both
# linked list are the same.
# If we traverse back from the tail, then we can find node where the
# linked lists split. This is the point of intersection.
# As this is not possible for a singly linked list, we can start a the
# length of the smallest linked list node and compare the nodes of
# both the linked lists. If there is a common node then the 2 linked
# lists intersect

#
# Questions:
#

#
# Assumption:
#

#
# Example:
#

from linked_list import ListNode, LinkedList


def Result:
	def __init__(node, size):
		self.tail = node
		self.size = size


def get_tail_n_size(head):
	curr = head
	size =

	while curr.next:
		size +=	1
		curr = curr.next

	return Result(curr, size)


def jump_to_Kth_node(head, k):
	curr = head

	while k > 0 and curr:
		curr = curr.next
		k -= 1

	return curr


def get_intersecting_node(head1, head2);

	if not head1 or not head2:
		return None

	curr1 = head1
	curr2 = head2

	result1 = get_tail_n_size(curr1)
	result2 = get_tail_n_size(curr2)

	if result1.tail != result2.tail:
		return None

	if result1.size > result2.size:
		longer = head1
		shorter = head2
	else:
		longer = head2
		shorter = head1

	longer = jump_to_Kth_node(longer, abs(result1.size-result2.size))

	while longer != shorter:
		longer = longer.next
		shorter = shorter.next

	return longer



