#
# Sum Lists
# You have two numbers represented by linked list, where each node
# contains a single digit. The digits are stored in reverse order,
# such that the 1's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a
# linked list. (You are not allowed to cheat and just convert the
# linked list to an integer)
# */

# /*
# Explaination:
# Sol3 --> Recursive sol for problem
# FOLLOW UP
# Invert both LLs and then add using first solution
# */

# /*
# Questions:
# 1) Can the LL contain -ve numbers?
# 2) Can any of the 2 LLs be null?
# */

# /*
# Assumption:
# 1) LL contains only non -ve numbers
# 2) LL contains atleast 0 or null.
# 3) Both LL contain only numbers.
# */

# /*
# Example:
# 1)  + 1->2 => 1->2
# 2) 0 + 1->2 => 1->2
# 3) 1->2-3 + 4->5->6 => 5->7->9
# 4) 9->9 + 1 => 0->0->1
# 5) 9->9 + 9->9 => 8->9->1
# 6) 1 + 9->9 => 0->0->1
# */

from linked_list import ListNode, LinkedList

def add_values(num1=0, num2=0, num3=0):
	total = num1 + num2 + num3
	return (total % 10, total // 10 )

def sum_linked_list(head1, head2):

	if not head1  and head2:
		return head2
	elif not head2 and head1:
		return head1

	sum_total = 0
	sum_d = 0
	carry = 0
	total_ll = LinkedList()

	while head1 and head2:
		sum_d, carry = add_values(head1.value, head2.value, carry)
		total_ll.add(sum_d)

		head1 = head1.next
		head2 = head2.next

	while head1 and not head2:
		sum_d, carry = add_values(head1.value, carry)
		total_ll.add(sum_d)
		head1 = head1.next

	while not head1 and head2:
		sum_d, carry = add_values(head2.value, carry)
		head2 = head2.next

	if carry:
		total_ll.add(carry)

	return total_ll.head


ll1 = LinkedList()
ll1.add_multiple([1,2,3])
ll2 = LinkedList()
ll2.add_multiple([3,2,1])
ll3 = LinkedList()
ll3.head = sum_linked_list(ll1.head, ll2.head)
print(ll3)

ll1.clear()
ll3 = LinkedList()
ll3.head = sum_linked_list(ll1.head, ll2.head)
print(ll3)

ll1.add_multiple([1,2,3])
ll2.clear()
ll2.add(0)
ll3.head = sum_linked_list(ll1.head, ll2.head)
print(ll3)

ll1.clear()
ll1.add_multiple([9,9,9])
ll2.clear()
ll2.add(1)
# ll3 = LinkedList
ll3.head = sum_linked_list(ll1.head, ll2.head)
print(ll3)

ll1.clear()
ll1.add_multiple([9,9])
ll2.clear()
ll2.add_multiple([9,9])
# ll3 = LinkedList
ll3.head = sum_linked_list(ll1.head, ll2.head)
print(ll3)
