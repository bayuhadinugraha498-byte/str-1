class Node(object):
	def __init__(self, d):
		self.data = d
		self.next_node = None

class Stack(object):
	def __init__(self):
		self.top = None
		self.size = 0
	def push(self, d):
		new_node = Node(d)
		if self.top:
			new_node.next_node = self.top
		self.top = new_node
		self.size += 1
	def pop(self):
		if self.top is None:
			return None
		result = self.top.data
		self.top = self.top.next_node
		self.size -= 1
		return result
	def peek(self):
		if self.top is None:
			return None
		return self.top.data
	def is_empty(self):
		if self.top is None:
			return True
		else:
			return False
		# or simply:
		# return self.top is None
# ===== PERINTAH UNTUK MENJALANKAN =====

stack = Stack()

# Menambah data ke stack
stack.push(10)
stack.push(20)
stack.push(30)

print("=== Uji Coba Stack ===")
print(f"Ukuran stack     : {stack.size}")         # 3
print(f"Peek (teratas)   : {stack.peek()}")        # 30
print(f"Stack kosong?    : {stack.is_empty()}")    # False

print("\n--- Pop satu per satu ---")
print(f"Pop ke-1: {stack.pop()}")   # 30
print(f"Pop ke-2: {stack.pop()}")   # 20
print(f"Pop ke-3: {stack.pop()}")   # 10
print(f"Pop ke-4: {stack.pop()}")   # None (stack kosong)

print(f"\nStack kosong sekarang? : {stack.is_empty()}")  # TrueA