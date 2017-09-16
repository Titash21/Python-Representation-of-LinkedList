import java.util.*;

/**
 * Created by TITASH MANDAL on 9/16/2017.
 */

public class AddTwoNumbersLinkedList {
    public static void main(String[] args) {
        List<Integer> list1=new LinkedList<>();
        List<Integer> list2=new LinkedList<>();
        List<Integer> result=new LinkedList<>();
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the length of first list: ");
        int size1=sc.nextInt();
        for(int i=0;i<size1;i++){
            System.out.println("Enter Item for list1: ");
            list1.add(sc.nextInt());
        }
        System.out.println("Enter the length of second list: ");
        int size2=sc.nextInt();
        for(int i=0;i<size2;i++){
            System.out.println("Enter Item for list1: ");
            list2.add(sc.nextInt());
        }



        Iterator iteratorList1=list1.iterator();
        Iterator iteratorList2=list2.iterator();
        System.out.println("List 1");
        while(iteratorList1.hasNext()){
            System.out.print(iteratorList1.next()+" ");
        }
        System.out.println();
        System.out.println("List 2: ");

        while(iteratorList2.hasNext()){
            System.out.print(iteratorList2.next()+" ");
        }

        System.out.println();
        int sizeList1=list1.size();
        int sizeList2=list2.size();
        int carry=0;
        int remainder;
        while(sizeList1>0 && sizeList2>0){

            int sum=carry+(list1.get(sizeList1-1)+list2.get(sizeList2-1));

            if(sum>9){
                carry=sum/10;
                remainder=sum%10;
                result.add(remainder);
                System.out.println("carry "+carry+"remainder "+remainder);
            }
            else{
                carry=0;
                result.add(sum);
                System.out.println(sum);
            }

            sizeList1--;
            sizeList2--;

        }
        while(sizeList1>0){
            int sum=carry+list1.get(sizeList1-1);
            result.add(sum);
            carry=0;
            sizeList1--;
        }
        while(sizeList2>0){
            int sum=carry+list2.get(sizeList2-1);
            result.add(sum);
            carry=0;
            sizeList2--;
        }

        Collections.reverse(result);
        System.out.println("RESULT");
        Iterator resultIterator=result.iterator();
        while(resultIterator.hasNext()){
            System.out.print(resultIterator.next()+" ");
        }


    }


}
