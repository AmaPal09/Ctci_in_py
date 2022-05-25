#
# Palindrome
# Implement function to check if a linked list is a palindrome
#

#
# Explaination:
# Store reversed verion of curr LL in another LL.
# Compare the inpout LL with the reversed LL.
# If both match, LL is a palindrome.
#

#
# Questions:
#

#
# Assumption:
#

#
# Example:
#
# 1 -> 2 -> 3 -> 4  ->
# Null <- 1 1->2 -> 3 ->
# Null<-1<-2
from linked_list import ListNode, LinkedList


def reverse_ll(head):
	prev = None
	curr = head

	while curr:
		temp = ListNode(curr.value)
		temp.next = prev
		prev = temp
		curr = curr.next

	return temp



def check_if_palindrome(head1, head2):
	if not head1 or not head2:
		return False

	head1 = reverse_ll(head1)

	while head1 and head2:
		if head1.value != head2.value:
			return False
		head1 = head1.next
		head2 = head2.next

	if head1 and not head2:
		return False
	elif head2 and not head1:
		return False
	else:
		return True


