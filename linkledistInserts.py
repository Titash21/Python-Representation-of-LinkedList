class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
#Insert Values at the front of the list
    def insert_at_front(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
#Insert at the end of the list
    def insert_at_back(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            new_node=Node(data)
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=new_node
#Insert a value at the given position mentioned. If the position is larger than the size
#of the Linked_List , insert it at the end of the linkedlist
    def insert_at_position(self,data,position):
        if self.head==None:
            self.head=Node(data)
        else:
            counter=1
            current=self.head
            new_node=Node(data)
            if(position==0):
                insert_at_front(data)
            else:
                while(current.next!=None and counter<position-1):
                    current=current.next
                    counter+=1
                new_node.next=current.next
                current.next=new_node

    def prints(self):
        if self.head==None:
            print("Empty linked list")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next

objects=Linked_List()

def main():
    print("OPTIONS FOR THIS PROGRAM")
    print("1. To insert at front")
    print("2. To insert at the end")
    print("3.To insert at any position")
    print("4. Delete a particular node")
    print("5. print contents of the linked list")
    choice=int(input("Enter now: "))
    if (choice>4):
        print("Wrong input! Exiting..........")
    else:
        driver_function(choice)

def driver_function(choice):
    if(choice==1):
        value=int(input("enter data to add in front: "))
        objects.insert_at_front(value)
        objects.prints()
    elif(choice==2):
        value=int(input("enter data to add at the end: "))
        objects.insert_at_back(value)
        objects.prints()
    elif(choice==3):
        value=int(input("enter data to add : "))
        position=int(input("enter the position to enter the value at: "))
        objects.insert_at_position(value,position)
        objects.prints()
    elif(choice==4):
        objects.prints()
    loops=int(input("want to enter again? then print 1 or 0: "))
    if(loops==1):
            main()
    else:
        objects.prints()


main()
