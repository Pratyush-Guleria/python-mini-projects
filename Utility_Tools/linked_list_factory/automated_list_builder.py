# =================================================================
# PROJECT: Automated Linked List Factory
# DESCRIPTION: A utility tool to automatically convert a Python List 
#              (Array) into a Linked List and visualize it.
# =================================================================

# 1. Define the Blueprint of a single block (Node)
class Node:
    def __init__(self, data):
        self.data = data    # Storing the actual value
        self.next = None    # Pointer to the next node in line

# --- UTILITY FUNCTION 1: The Builder ---
# This function automates the process of linking nodes using a loop.
def create_linked_list(arr):
    if not arr: 
        return None  # Return None if the input list is empty

    # Step A: Create the "Head" (Engine) of the train
    head = Node(arr[0]) 
    current = head # 'current' acts as the driver to move through the chain

    # Step B: Iterate through the rest of the list and link them automatically
    for value in arr[1:]:
        current.next = Node(value) # Create a new node and tie it to the last one
        current = current.next     # Move the driver to the newly added node
    
    return head # Return the starting point of the automated list

# --- UTILITY FUNCTION 2: The Visualizer ---
# This function handles the printing logic so you don't have to write loops manually.
def display_list(head):
    temp = head
    print("Automated Linked List Output:", end=" ")
    while temp:
        print(f"{temp.data} ->", end=" ")
        temp = temp.next
    print("None")

# =================================================================
# TESTING THE FACTORY TOOL
# =================================================================
if __name__ == "__main__":
    # You can put 10 or 10,000 numbers here; the tool will handle it!
    test_data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    # Step 1: Use the Factory to build the list
    linked_list_head = create_linked_list(test_data)

    # Step 2: Use the Visualizer to see the result
    display_list(linked_list_head)
