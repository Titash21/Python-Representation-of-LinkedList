/**
 * Created by TITASH MANDAL on 9/16/2017.
 */
class Node{
    int data;
    Node next;
    public Node(int data){
        this.data=data;
        this.next=null;
    }
        }
public class GetMergeOfLinkedList {
    Node headA;
    Node headB;
    public GetMergeOfLinkedList(){
        this.headA=null;
        this.headB=null;
    }

    int getLength(Node head){
        int count=0;
        if(head==null){
            return -1;
        }
        else{

            while(head!=null){
                count++;
                head=head.next;
            }

        }
        return count;
    }

    int getMergePoint(int diff,Node headH,Node headL){

        for(int i=0;i<diff;i++){
            headH=headH.next;
        }
        while(headH!=null && headL!=null){
            if(headH.equals(headL)){
                return headH.data;
            }
            else{
                headH=headH.next;
                headL=headL.next;
            }
        }
        return -1;
    }
    int FindMergeNode(Node headA, Node headB) {
        // Complete this function
        // Do not write the main method.
        int lengthA=getLength(headA);
        int lengthB=getLength(headB);
        if(lengthA==-1 || lengthB==-1){
            return 0;
        }
        else{
            if(lengthA>=lengthB){
                int difference=lengthA-lengthB;
                return(getMergePoint(difference,headA,headB));
            }
            else{
                int difference=lengthB-lengthA;
                return(getMergePoint(difference,headB,headA));
            }
        }


    }
}
