#A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
def has_cycle(head):
    if head==None:
        return 0
    else:
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return 1
        return 0
