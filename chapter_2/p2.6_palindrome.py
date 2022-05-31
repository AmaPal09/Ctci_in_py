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
import unittest

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


class Test(unittest.TestCase):
	test_cases = [
		([1,2,3], [3,2,1], True),
		([1,2,3,4], [2,1,3,4], False),
	]

	test_functions = [
		check_if_palindrome,
	]

	def test_check_if_palindrome(self):
		for f in self.test_cases:
			for h1, h2, expected in self.test_cases:
				head1_ll = LinkedList(h1)
				head2_ll = LinkedList(h2)

				assert check_if_palindrome(head1_ll.head, head2_ll.head) == expected


class Test2(unittest.TestCase):
	test_cases = [
		([1,2,3,4], [4,3,2,1]),
	]

	test_functions = [
		reverse_ll
	]

	def test_reverse_ll(self):
		for f in self.test_cases:
			for case, expected in self.test_cases:
				case_ll = LinkedList(case)
				result = LinkedList()
				result.head = reverse_ll(case_ll.head)
				assert result.values() == expected


if __name__ == "__main__":
	unittest.main()