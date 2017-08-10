class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_List:
    def __init__(self):
        self.head=None
    def compare_list(self):
        head1=objects1.head_extract()
        head2=objects2.head_extract()
        while(head1!=None and head2!=None):
            if(head2.data==head1.data):
                head1=head1.next
                head2=head2.next
                continue
            else:
                return 0
                #if the lists are of unequal length
        if (head1==None and head2!=None):
            return 0
            #if the lists are of unequal length
        elif (head2==None and head1!=None):
            return 0
            #the end of the list is reached and their data is equal
        elif(head1==None and head2==None):
            return 1

    def insert_at_front(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
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

objects1=Linked_List()
objects2=Linked_List()
objects=Linked_List()

def main():
    value=int(input("enter size of the first list: "))
    for i in range(value):
        data=int(input("enter: "))
        objects1.insert_at_front(data)
    objects1.prints()
    value=int(input("enter size of the second list: "))
    for i in range(value):
        data=int(input("enter: "))
        objects2.insert_at_front(data)
    objects2.prints()
    value_Ret=objects.compare_list()
    if(value_Ret==1):
        print("EQUAL LISTS")
    else:
        print("NOT EQUAL LISTS")
main()
