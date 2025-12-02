from linked_list.SinglyLinkedList import LinkedList
from linked_list.DoublyLinkedList import DoublyLinkedList
from linked_list.CircularLinkedList import CircularLinkedList

ll = LinkedList()
dll = DoublyLinkedList()
cll = CircularLinkedList()

def linked_list():
    ll.insert_end(12)
    ll.insert_end(13)
    ll.insert_end(14)
    ll.insert_first(1)
    print(f'length of the Linked list: {ll.length()}')
    # ll.insertAt_index(5,2)
    # print(ll.delete_first())
    # print(ll.delete_last())
    print(ll.delete_node_by_value(5))
    ll.print_linked_list()


def doubly_linked_list():
    dll.insert_first(2)
    dll.insert_first(1)
    dll.insert_last(4)
    dll.insert_index(2,3)
    print(dll.delete_first())
    print(dll.delete_last())
    print(dll.delete_index(1))
    dll.print()

def cirular_linked_list():
    cll.insert_first(4)
    cll.insert_first(3)
    cll.insert_first(2)
    cll.insert_first(1)
    cll.insert_last(5)
    cll.insert_last(6)
    cll.insert_index(2,10)
    # cll.delete_first()
    print(cll.delete_last())
    cll.print()



linked_list()
# doubly_linked_list()
# cirular_linked_list()