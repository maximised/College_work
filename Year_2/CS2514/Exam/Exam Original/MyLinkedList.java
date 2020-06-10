/**
 * Question 4: Linked Lists. 
 * The List class is named MyLinkedList to avoid confusion with the already implemented List interface
 *
 * @author: (118364841)
 */
import java.util.*;

public class MyLinkedList<T extends Comparable<T>> implements Iterable<T> {
    private Link<T> nodes;
    
    public MyLinkedList( ) {
        nodes = null;
    }

    public void add( final T item ) {
        nodes = new Link<T>( item, nodes );
    }

    public T getHead( ) {
        return nodes.getHead( ); 
    }

    public void print( ) {
        for ( T node : this ) {
            System.out.print( node + " ");
        } 
        System.out.println();
    }

    public static <T extends Comparable<T>> void qsort( final MyLinkedList<T> list ) {
        list.nodes = Link.qsort( list.nodes );
    }

    @Override
    public Iterator<T> iterator() {
        return Link.iterator( nodes );
    }
}
