class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Merge:
    def __init__(self):
        self.head=None
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

    def prints(self):
        if self.head==None:
            print("Empty linked list")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def head_extract(self):
        return self.head
        #merge two lists
    def MergeLists(self,objects1, objects2):
        headA=objects1.head_extract()
        headB=objects2.head_extract()
        if headA==None and headB!=None:
            return headB
        elif headB==None and headA!=None:
            return headA
        elif headA==None and headB==None:
            return None
        else:
            currentA=headA
            currentB=headB
            head=None
            if (headA.data<headB.data):
                head=Node(headA.data)
                currentA=headA.next
            else:
                head=Node(headB.data)
                currentB=headB.next

            temp=head

            #Two lists present
            while(currentA!=None and currentB!=None):
                if(currentA.data<=currentB.data):
                    temp.next=currentA.data
                    currentA=currentA.next
                    temp=temp.next

                elif(currentB.data<currentA.data):
                    temp.next=currentB.data
                    currentB=currentB.next
                    temp=temp.next
        
            if(currentA==None and currentB!=None):
                while(currentB!=None):
                    temp.next=currentB.data
                    currentB=currentB.next
                    temp=temp.next

            elif(currentA!=None and currentB==None):
                while(currentA!=None):
                    temp.next=currentA.data
                    currentA=currentA.next
                    temp=temp.next
            print(head.data)
            print(head.next)
            while(head.next!=None):
                print(head.data)
                head=head.next


objects1=Merge()
objects2=Merge()
objects=Merge()
def main():
    print("OPTIONS FOR THIS PROGRAM")
    print("1. Enter first Linked_List")
    print("2. Enter second Linked_List")
    print("3. Merge sorted lists")
    choice=int(input("Enter now: "))
    if (choice>4):
        print("Wrong input! Exiting..........")
    else:
        driver_function(choice)
def driver_function(choice):
    if(choice==1):
        value=int(input("enter length of the first sorted linkedList: "))
        while(value>0):
            objects1.insert_at_back(int(input("Enter the value: ")))
            objects1.prints()
            value-=1

    elif(choice==2):
        value=int(input("enter length of the second sorted linkedList: "))
        while(value>0):
            objects2.insert_at_back(int(input("Enter the value: ")))
            objects2.prints()
            value-=1

    elif(choice==3):
        objects.MergeLists(objects1,objects2)
        print("Printing the mergd list")


    loops=int(input("want to enter again? then print 1 or 0: "))
    if(loops==1):
            main()
    else:
        objects.prints()


main()
