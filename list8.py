# Queue Implementation using List

queue = []

while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue (Insert)")
    print("2. Dequeue (Delete)")
    print("3. Display")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    # Enqueue Operation
    if choice == 1:
        element = input("Enter element to insert: ")
        queue.append(element)
        print(element, "inserted into queue")
    
    # Dequeue Operation
    elif choice == 2:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            removed = queue.pop(0)
            print(removed, "removed from queue")
    
    # Display Operation
    elif choice == 3:
        if len(queue) == 0:
            print("Queue is Empty")
        else:
            print("Queue elements are:")
            for item in queue:
                print(item)
    
    # Exit
    elif choice == 4:
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice! Please try again.")
