class stack:
	def __init__(self, size):
		self.size = size
		self.pointer = 0
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

	def push(self, value):
		if not self.full():
			self.items[self.pointer] = value
			self.pointer += 1
			return value
		else:
			print(f"Stack is full, cannot push \"{value}\"")
			return None

	def pop(self):
		if not self.empty():
			self.pointer -= 1
			popped = self.items[self.pointer]
			self.items[self.pointer] = None
			return popped
		else:
			print("Stack is empty, cannot pop")
			return None

	def clear(self):
		self.items = [None for i in range(self.size)]
		self.pointer = 0
		return "Cleared"

	def empty(self):
		return self.items[0] == None

	def full(self):
		return self.pointer >= self.size


var = stack(5)

print(var)
print(f"Empty: {var.empty()}")
print(f"Full: {var.full()}")
print()
print(f"Pushed: \"{var.push('hi')}\"")
print(var)
print(f"Empty: {var.empty()}")
print(f"Full: {var.full()}")
print()
print(f"Popped: \"{var.pop()}\"")
print(var)
print(f"Empty: {var.empty()}")
print(f"Full: {var.full()}")
print()
print()
print(f"Pushed: \"{var.push('1')}\"")
print(f"Pushed: \"{var.push('2')}\"")
print(f"Pushed: \"{var.push('3')}\"")
print(f"Pushed: \"{var.push('4')}\"")
print(f"Pushed: \"{var.push('5')}\"")
print(f"Pushed: \"{var.push('6')}\"")
print(var)
print(f"Empty: {var.empty()}")
print(f"Full: {var.full()}")
print()
print(var.clear())
print(var)
print(f"Empty: {var.empty()}")
print(f"Full: {var.full()}")
print()