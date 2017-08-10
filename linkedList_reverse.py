class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
#Insert the data at the front of the Linked_List
    def insert_at_front(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
#Delete the data if present in the linked list
    def reverse_linkedList(self):
        if self.head==None:
            print(None)
        else:
            p=self.head
            r=None
            while(p.next!=None):
                q=p
                p=p.next
                q.next=r
                r=q
        p.next=r
        self.head=p

    def reverse_linkedList_recursive(self,head):
         if self.head:
             reverse_linkedList_recursive(self.head.next)
             print(self.head.data)


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
    print("2. Reverse a particular list non recursively")
    print("3. Reverse a particular list recursively")
    print("4. Print contents of the linked list")
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
        objects.reverse_linkedList()
        objects.prints()
    elif(choice==3):
        objects.reverse_linkedList_recursive()
        objects.prints()
    elif(choice==4):
        objects.prints()

    loops=int(input("want to enter again? then print 1 or 0: "))
    if(loops==1):
            main()
    else:
        objects.prints()


main()
