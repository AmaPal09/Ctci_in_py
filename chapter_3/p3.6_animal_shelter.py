#
# Animal Shelter
# An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.
#

#
# Explaination:
# "Oldest" (based on arrival time.) So a normal queue should work here for current scenario.
#

#
# Questions:
# 1)
#

#
# Assumption:
# 1)
#

#
# Example:
# 1)
#

class Animal():
	def __init__(self, name, typeAnimal):
		self._name = name
		self._type = typeAnimal


class Queue():
	def __init__(self):
		self._queue = []

	def size(self):
		return len(self._queue)

	def isEmpty(self):
		return self.size() == 0

	def enqueue(self, val):
		self._queue.append(val)

	def peek(self):
		if self.isEmpty():
			return None
		else:
			return self._queue[0]

	def dequeue(self):
		if self.isEmpty():
			return None
		else:
			return self._queue.pop(0)


class AnimalShelter():
	def __init__(self):
		self._all = Queue()
		self._cats = Queue()
		self._dogs = Queue()

	def enqueue(self, animal):
		if animal._type == "dog":
			self._dogs.enqueue(animal)
			self._all.enqueue(animal)
		elif animal._type == "cat":
			self._cats.enqueue(animal)
			self._all.enqueue(animal)

	def dequeueCat(self):
		if self._cats.isEmpty():
			return None
		else:
			self._cats.dequeue()
			return self._all.dequeue()

	def dequeueDog(self):
		if self._dogs.isEmpty():
			return None
		else:
			self._dogs.dequeue()
			return self._all.dequeue()

	def dequeueAny(self):
		if self._dogs.peek() == self._all.peek():
			return self.dequeueDog()
		else:
			return self.dequeueCat()

harry = Animal("Harry", "cat")
ron = Animal("Ron", "dog")
hagrid = Animal("Hagrid", "dog")
hermione = Animal("Hermione", "cat")
jinny = Animal("Jinny", "dog")
mcgonagall = Animal("McGonagall", "cat")
snape = Animal("Snape", "dog")

a1 = AnimalShelter()
a1.enqueue(mcgonagall)
a1.enqueue(hagrid)
a1.enqueue(snape)
a1.enqueue(hermione)
a1.enqueue(harry)
a1.enqueue(ron)
a1.enqueue(jinny)
print(a1._all._queue)
print(a1._cats._queue)
print(a1._dogs._queue)
print(a1.dequeueAny()._name)
print(a1.dequeueCat())
print(a1.dequeueDog())
print(a1._all._queue)
print(a1._cats._queue)
print(a1._dogs._queue)

