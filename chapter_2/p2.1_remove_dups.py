#
# Remove Dups
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# how will you solve this problem if a temp buffer is not allowed
#

#
# Explaination:
#

#
# Questions:
# 1) What about nodes with " "?
#

#
# Assumption:
# 1) Function is passed the head of the linked list.
# 2) Not a method on the LL class
#

class ListNode:
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next = next_node

	def __str__(self):
		return str(self.value)


def remove_dups(head):
	curr_node = head
	prev_node = None
	node_set = set()

	while curr_node:
		if curr_node.value in node_set:
			prev_node.next = curr_node.next
			curr_node = curr_node.next
		else:
			node_set.add(curr_node.value)
			prev_node = curr_node
			curr_node = curr_node.next

	return head


h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(1, ListNode(4)))))

def print_ll(head):
	ll_array = []
	curr = head
	while curr:
		ll_array.append(curr.value)
		curr = curr.next
	print("->".join(str(val) for val in ll_array))

print_ll(h1)
remove_dups(h1)
print_ll(h1)


def remove_dups_2(head):
	curr_node = head

	while curr_node:
		runner_node = curr_node

		while runner_node.next:
			if runner_node.next.value == curr_node.value:
				runner_node.next = runner_node.next.next
			else:
				runner_node = runner_node.next

		curr_node = curr_node.next

h1 = ListNode(1, ListNode(2, ListNode(3, ListNode(1, ListNode(4)))))
print_ll(h1)
remove_dups(h1)
print_ll(h1)