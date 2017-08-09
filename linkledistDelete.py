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
    def delete_value_linkedList(self,data):
        if self.head==None:
            print("You are trying to delete from an empty list")
        elif(self.head.data==data):
            self.head=self.head.next

        else:
            temp=self.head
            prev=self.head
            while(temp.next!=None and temp.data!=data):
                prev=temp
                temp=temp.next
            if(temp.data!=data and temp.next==None):
                print("The data you want to delete is not in the list")
            prev.next=temp.next
            temp=None




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
    print("2. Delete a particular node")
    print("3. print contents of the linked list")
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
        value=int(input("enter data to delete: "))
        objects.delete_value_linkedList(value)
        objects.prints()

    elif(choice==3):
        objects.prints()

    loops=int(input("want to enter again? then print 1 or 0: "))
    if(loops==1):
            main()
    else:
        objects.prints()


main()
