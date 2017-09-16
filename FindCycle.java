/**
 * Created by TITASH MANDAL on 9/16/2017.
 */
class Nodes {
    int data;
    Nodes next;

    public Nodes(int data) {
        this.data = data;
        this.next = null;
    }
}

public class FindCycle {
    //Return 1 if cycle is found else return 0.
    int findCycle(Node head){
        if(head==null){
            return -1;
        }
        else{
            Node fast=head;
            while(fast!=null && fast.next!=null){
                fast=fast.next.next;
                head=head.next;
                if(head.equals(fast)){
                    return 1;
                }
            }
        }
        return 0;
    }

}

