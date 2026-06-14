class Node:
    def __init__(self, order_id: str, num_pages: int, is_tahap2: bool = False):
        self.order_id = order_id
        self.num_pages = num_pages
        self.is_tahap2 = is_tahap2
        self.next = None


class QueueFotokopi:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    @staticmethod
    def buat_order_id(nama: str, nim: str) -> str:
        huruf = "".join(c for c in nama if c.isalpha())[:3].upper()
        digit = nim[-2:]
        return huruf + digit

    def _append(self, node: Node) -> None:
        if self._rear is None:
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def enqueue(self, order_id: str, num_pages: int) -> None:
        self._append(Node(order_id, num_pages))
        print(f" [ENQUEUE] '{order_id}' ({num_pages} hal.) -> masuk antrian.")

    def dequeue(self):
        if self.is_empty():
            print(" [DEQUEUE] Antrian kosong.")
            return None

        node = self._front
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1

        order_id = node.order_id
        num_pages = node.num_pages

        if num_pages > 100 and not node.is_tahap2:
            print(f" [DEQUEUE] '{order_id}' ({num_pages} hal.) -> TAHAP 1 selesai. "
                  f"Dikembalikan ke antrian untuk TAHAP 2.")
            tahap2_node = Node(order_id, num_pages, is_tahap2=True)
            self._append(tahap2_node)
        elif node.is_tahap2:
            print(f" [DEQUEUE] '{order_id}' ({num_pages} hal.) -> TAHAP 2 selesai. "
                  f"Pesanan tuntas.")
        else:
            print(f" [DEQUEUE] '{order_id}' ({num_pages} hal.) -> Selesai dilayani.")

        return (order_id, num_pages)

    def fast_track(self, order_id: str, num_pages: int) -> None:
        if num_pages < 10:
            print(f" [FAST TRACK] '{order_id}' ({num_pages} hal.) "
                  f"-> langsung diproses tanpa antri! ✓")
        else:
            print(f" [FAST TRACK] '{order_id}' ({num_pages} hal.) "
                  f"tidak memenuhi syarat fast track (≥ 10 hal.). Masuk antrian biasa.")
            self.enqueue(order_id, num_pages)

    def front(self):
        if self.is_empty():
            print(" [FRONT] Antrian kosong.")
            return None
        label = " [Tahap 2]" if self._front.is_tahap2 else ""
        print(f" [FRONT] '{self._front.order_id}' ({self._front.num_pages} hal.){label}")
        return (self._front.order_id, self._front.num_pages)

    def rear(self):
        if self.is_empty():
            print(" [REAR] Antrian kosong.")
            return None
        label = " [Tahap 2]" if self._rear.is_tahap2 else ""
        print(f" [REAR] '{self._rear.order_id}' ({self._rear.num_pages} hal.){label}")
        return (self._rear.order_id, self._rear.num_pages)

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def tampilan_antrian(self) -> None:  # ← nama ini yang benar
        if self.is_empty():
            print(" [ANTRIAN] (kosong)")
            return
        cur, items = self._front, []
        while cur:
            tag = " [T2]" if cur.is_tahap2 else ""
            items.append(f"'{cur.order_id}'{tag} ({cur.num_pages} hal)")
            cur = cur.next
        print(f" [ANTRIAN] {self._size} pesanan: " + " -> ".join(items))


if __name__ == "__main__":
    q = QueueFotokopi()

    data = [
        ("Bagus Wibowo",        "2026001234", 50),
        ("Rina Dwi Rahmadhani", "2026005678", 120),
        ("Ari Santoso",         "2026009012", 8),
        ("Siti Rohmah Ayu",     "2026003456", 80),
        ("Doni Kurniawan",      "2026007890", 15),
        ("Bayu Hadi Nugraha",   "2025002345", 110),
    ]

    SEP = "=" * 60

    print(SEP)
    print("SISTEM ANTRIAN LAYANAN FOTOKOPI KAMPUS")
    print(SEP)

    print("\n▶ TAHAP 1 -- Mendaftarkan pesanan")
    print("-" * 60)
    for nama, nim, halaman in data:
        oid = QueueFotokopi.buat_order_id(nama, nim)
        print(f"\n Nama : {nama}")
        print(f" NIM  : {nim} | ID: {oid} | Halaman: {halaman}")
        if halaman < 10:
            q.fast_track(oid, halaman)
        else:
            q.enqueue(oid, halaman)

    print("\n▶ TAHAP 2 - Informasi antrian")
    print("-" * 60)
    q.tampilan_antrian()   # ← diperbaiki
    q.front()              # ← diperbaiki (font -> front)
    q.rear()
    print(f" [SIZE]     Jumlah pesanan  : {q.size()}")
    print(f" [IS_EMPTY] Antrian kosong? : {q.is_empty()}")

    print("\n▶ TAHAP 3 - Memproses pesanan (dequeue)")
    print("-" * 60)
    langkah = 1
    while not q.is_empty():
        print(f"\n [Langkah {langkah}]")
        q.dequeue()
        q.tampilan_antrian()
        langkah += 1

    print("\n▶ TAHAP 4 - Kondisi akhir")
    print("-" * 60)
    print(f" [IS_EMPTY] Antrian Kosong? : {q.is_empty()}")
    print(f" [SIZE]     Sisa pesanan   : {q.size()}")  # ← diperbaiki (siz -> size)
    print("\n ✓ Semua pesanan selesai diproses!")
    print(SEP)