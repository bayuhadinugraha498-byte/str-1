class Node(object):
	def __init__(self, d):
		self.data = d
		self.prev_node = None
		self.next_node = None

class Queue(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0
	def enqueue(self, d):
		new_node = Node(d)
		if self.size > 0:
			self.tail.prev_node = new_node
			new_node.next_node = self.tail
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node
		self.size += 1
	def dequeue(self):
		if self.head == None:
			return None
		result = self.head
		self.head = self.head.prev_node
		self.size -= 1
		return result.data
	def peek(self):
		if self.head:
			return self.head.data
		return None
	def get_size(self):
		return self.size
# ===== PERINTAH UNTUK MENJALANKAN =====

queue = Queue()

# Menambah data ke queue
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)

print("=== Uji Coba Queue ===")
print(f"Ukuran queue     : {queue.get_size()}")      # 3
print(f"Peek (terdepan)  : {queue.peek()}")          # 40
print(f"Queue kosong?    : {queue.get_size() == 0}") # False

print("\n--- Dequeue satu per satu ---")
print(f"Dequeue ke-1: {queue.dequeue()}")  # 40
print(f"Dequeue ke-2: {queue.dequeue()}")  # 50
print(f"Dequeue ke-3: {queue.dequeue()}")  # 60
print(f"Dequeue ke-4: {queue.dequeue()}")  # None (queue kosong)

print(f"\nQueue kosong sekarang? : {queue.get_size() == 0}")  # True