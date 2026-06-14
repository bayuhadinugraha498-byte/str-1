class Node(object):
    def __init__(self, d):
        self.next_node = None
        self.data = d


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add d to tail of list
    def add(self, d):
        new_node = Node(d)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    # Add d at specific index
    def add_at(self, d, index):
        if index < 0 or index > self.size:
            return False

        new_node = Node(d)

        if index == 0:  # Tambah di awal
            new_node.next_node = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            previous_node = None
            current_node = self.head
            i = 0
            while i < index and current_node:
                previous_node = current_node
                current_node = current_node.next_node
                i += 1

            previous_node.next_node = new_node
            new_node.next_node = current_node

            if new_node.next_node is None:  # Jika ditambahkan di akhir
                self.tail = new_node

        self.size += 1
        return True

    # Remove first occurrence of d
    def remove(self, d):
        previous_node = None
        current_node = self.head

        while current_node:
            if current_node.data == d:
                if previous_node:
                    previous_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node

                if self.head is None:  # List menjadi kosong
                    self.tail = None

                self.size -= 1
                return True

            previous_node = current_node
            current_node = current_node.next_node

        return False

    # Check if d exists in list
    def find(self, d):
        current_node = self.head
        while current_node:
            if current_node.data == d:
                return True
            current_node = current_node.next_node
        return False

    # Convert linked list to Python list
    def to_list(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next_node
        return result


# ====================== TEST PROGRAM ======================
if __name__ == "__main__":
    ll = LinkedList()

    ll.add(10)
    ll.add(20)
    ll.add(30)
    ll.add(40)

    print("Isi Linked List     :", ll.to_list())
    print("Ukuran Linked List  :", ll.size)

    ll.add_at(25, 2)      # sisipkan 25 di index ke-2
    print("Setelah add_at(25,2):", ll.to_list())

    ll.add_at(5, 0)       # sisipkan 5 di awal
    print("Setelah add_at(5,0) :", ll.to_list())

    print("Apakah 30 ada?      :", ll.find(30))
    print("Apakah 99 ada?      :", ll.find(99))

    ll.remove(20)
    print("Setelah remove(20)  :", ll.to_list())

    ll.remove(100)        # data yang tidak ada
    print("Setelah remove(100) :", ll.to_list())
