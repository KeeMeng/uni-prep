class queue:
	def __init__(self, size):
		self.size = size
		self.head = 0
		self.tail = 0
		self.items = [None for i in range(self.size)]

	def __repr__(self):
		string = ""
		for i in self.items:
			if i != None:
				string += f"\"{i}\", "
			else:
				string += ", "
		return "[" + string[:-2] + "]"
	
	def __str__(self):
		string = ""
		for i in self.items:
			if i != None:
				string += f"\"{i}\", "
			else:
				string += f", "
		return "[" + string[:-2] + "]"
		
	def enqueue(self, value):
		if not self.full():
			self.items[self.tail] = value
			self.tail += 1
			if self.tail >= self.size:
				self.tail = 0
			return value
		else:
			print(f"Queue is full, cannot enqueue \"{value}\"")
			return None

	def dequeue(self):
		if not self.empty():
			value = self.items[self.head]
			self.items[self.head] = None
			self.head += 1
			if self.head >= self.size:
				self.head = 0
			return value
		else:
			print("Queue is empty, cannot dequeue")
			return None

	def clear(self):
		self.items = [None for i in range(self.size)]
		self.head = 0
		self.tail = 0
		return "Cleared"

	def empty(self):
		return self.head == self.tail and self.items[self.head] == None

	def full(self):
		return self.head == self.tail and self.items[self.head] != None

var = queue(5)
print(str(var) + " - queue(5)")
var.enqueue("a")
print(str(var) + " - enqueue('a')")
var.enqueue("b")
print(str(var) + " - enqueue('b')")
var.enqueue("c")
print(str(var) + " - enqueue('c')")
var.enqueue("d")
print(str(var) + " - enqueue('d')")
var.enqueue("e")
print(str(var) + " - enqueue('e')")
var.enqueue("f")
print(str(var) + " - enqueue('f')")
var.dequeue()
print(str(var) + " - dequeue()")
var.dequeue()
print(str(var) + " - dequeue()")
var.enqueue("g")
print(str(var) + " - enqueue('g')")
var.enqueue("h")
print(str(var) + " - enqueue('h')")
var.enqueue("i")
print(str(var) + " - enqueue('i')")
var.dequeue()
print(str(var) + " - dequeue()")
var.dequeue()
print(str(var) + " - dequeue()")
var.enqueue("j")
print(str(var) + " - enqueue('j')")
var.dequeue()
print(str(var) + " - dequeue()")
var.dequeue()
print(str(var) + " - dequeue()")
var.enqueue("k")
print(str(var) + " - enqueue('k')")
var.dequeue()
print(str(var) + " - dequeue()")
var.dequeue()
print(str(var) + " - dequeue()")
var.dequeue()
print(str(var) + " - dequeue()")