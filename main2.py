# main.py
from queue import Queue

def main():
    my_queue = Queue()

    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("0. Exit")

        choice = int(input("Pilih operasi (0-4): "))

        if choice == 0:
            print("Program selesai.")
            break
        elif choice == 1:
            data = int(input("Masukkan elemen yang ingin dienqueue: "))
            my_queue.enqueue(data)
            print(f"{data} telah dienqueue.")
        elif choice == 2:
            dequeued_item = my_queue.dequeue()
            if dequeued_item is not None:
                print(f"{dequeued_item} telah dikeluarkan dari antrian.")
            else:
                print("Antrian kosong.")
        elif choice == 3:
            front_element = my_queue.peek()
            if front_element is not None:
                print(f"Elemen terdepan: {front_element}")
            else:
                print("Antrian kosong.")
        elif choice == 4:
            print("Elemen dalam antrian:")
            my_queue.display()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
