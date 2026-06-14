from linked_list import LinkedList

# ── Node untuk Doubly Linked List ──────────────────────────────────────────────
class Node(object):
	def __init__(self, d):
		self.next_node = None
		self.prev_node = None
		self.data = d

# Keunggulan  : prev_node memungkinkan iterasi mundur yang efisien
#               dan operasi seperti delete lebih mudah (tanpa iterasi)
# Kekurangan  : Membutuhkan memori tambahan untuk pointer prev_node
class DoublyLinkedList(LinkedList):
	

	# remove_node menerima objek Node langsung →
	# langsung tahu prev_node & next_node tanpa iterasi
	def remove_node(self, node):
		if node is None:
			return False
		previous = node.prev_node
		if previous is None:
			# node adalah head
			self.head = node.next_node
			if self.head:
				self.head.prev_node = None
		else:
			previous.next_node = node.next_node
			if node.next_node:
				node.next_node.prev_node = previous
		# perbarui tail jika node yang dihapus adalah ekor
		if node.next_node is None:
			self.tail = previous
		self.size -= 1
		return True

	# add: mengembalikan objek Node dan mengatur prev_node
	def add(self, d):
		new_node = Node(d)
		if self.tail:
			new_node.prev_node = self.tail   # ← sambungkan prev
			self.tail.next_node = new_node
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node
		self.size += 1
		return new_node                      # ← satu-satunya baris berbeda
	
	def __len__(self):
		return self.size

	# Cetak list maju
	def print_forward(self):
		elements = []
		current = self.head
		while current:
			elements.append(str(current.data))
			current = current.next_node
		print("Maju  :", " <-> ".join(elements) if elements else "(kosong)")

	# Cetak list mundur (keunggulan DLL)
	def print_backward(self):
		elements = []
		current = self.tail
		while current:
			elements.append(str(current.data))
			current = current.prev_node
		print("Mundur:", " <-> ".join(elements) if elements else "(kosong)")
	
	


# ── Demo ───────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
	dll = DoublyLinkedList()

	print("=" * 45)
	print("       DEMO DOUBLY LINKED LIST")
	print("=" * 45)

	# 1. Tambah elemen
	print("\n[1] Menambahkan 10, 20, 30, 40, 50 …")
	node10 = dll.add(10)
	node20 = dll.add(20)
	node30 = dll.add(30)
	node40 = dll.add(40)
	node50 = dll.add(50)
	dll.print_forward()
	dll.print_backward()
	print(f"    Ukuran: {len(dll)}")

	# 2. Hapus node tengah (30) langsung via objek Node
	print("\n[2] Menghapus node 30 (langsung via objek Node) …")
	hasil = dll.remove_node(node30)
	print(f"    Berhasil dihapus: {hasil}")
	dll.print_forward()
	dll.print_backward()
	print(f"    Ukuran: {len(dll)}")

	# 3. Hapus head (10)
	print("\n[3] Menghapus head (10) …")
	dll.remove_node(node10)
	dll.print_forward()
	dll.print_backward()
	print(f"    Ukuran: {len(dll)}")

	# 4. Hapus tail (50)
	print("\n[4] Menghapus tail (50) …")
	dll.remove_node(node50)
	dll.print_forward()
	dll.print_backward()
	print(f"    Ukuran: {len(dll)}")

	# 5. Coba hapus node None
	print("\n[5] Mencoba hapus node None …")
	print(f"    Hasil: {dll.remove_node(None)}")

	# 6. Hapus semua sisa elemen
	print("\n[6] Menghapus semua sisa elemen (20, 40) …")
	dll.remove_node(node20)
	dll.remove_node(node40)
	dll.print_forward()
	print(f"    Ukuran: {len(dll)}")

	print("\n" + "=" * 45)
	print("  Selesai!")
	print("=" * 45)