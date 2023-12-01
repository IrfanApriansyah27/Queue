# main.py
from queue import Queue

def main():
    my_queue = Queue()

    # Enqueue beberapa elemen
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)

    # Tampilkan elemen dalam antrian
    print("Elemen dalam antrian:")
    my_queue.display()

    # Tampilkan elemen terdepan
    print("Elemen terdepan:", my_queue.peek())

    # Dequeue satu elemen
    dequeued_item = my_queue.dequeue()
    print("Elemen yang dikeluarkan:", dequeued_item)

    # Tampilkan elemen dalam antrian setelah dequeue
    print("Elemen dalam antrian setelah dequeue:")
    my_queue.display()

if __name__ == "__main__":
    main()
