def GetNode(head, position):
   #reverse the list and print from head
    p=head
    q=head
    r=None
    while(p.next!=None):
        q=p
        p=p.next
        q.next=r
        r=q
    p.next=r
    head=p
    if(position==0):
        return head.data
    else:
        temp=0
        while(head!=None and temp<=position-1):
            head=head.next
            temp=temp+1
        return head.data

        
