/**
 * This is the Main class where we instantiate and test all our classes we created
 *
 * @author: (118364841)
 */

/**
* Question 4: Linked Lists.
*/
import java.util.*;

public class Main {
    public static void main ( String[] args ) {

        MyLinkedList<Integer> mylist1 = new MyLinkedList<Integer>();
        mylist1.add( 11 );
        mylist1.add( 21 );
        mylist1.add( 50 );

        System.out.println( "My Linked List before quicksort:" );
        mylist1.print();
        System.out.println();

        System.out.println( "My Linked List after quicksort:" );
        MyLinkedList.qsort( mylist1 );
        mylist1.print();

    }
}