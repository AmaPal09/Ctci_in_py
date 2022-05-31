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





