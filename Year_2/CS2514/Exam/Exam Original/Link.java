/**
 * Question 4: Linked Lists. 
 * The Link of the List class
 *
 * @author: (118364841)
 */

import java.util.Iterator;

public class Link<T> implements Iterable<Link<T>> {

    private T head;
    private Link<T> tail;

    public Link( final T item, final Link<T> list ) {
        head = item;
        tail = list;
    }

    public T getHead( ) {
        return head;
    }

    public void setTail( final Link<T> list ) {
        this.tail = list;
    }

    public static <S> void print( final Link<S> list ) {
        Task<Link<S>> print1 = new Print1<S>();
        Traverser<Link<S>> linktraverser = new Traverser<Link<S>>( list );
        linktraverser.traverse( print1 );
    }
 
    public static <S extends Comparable<S>> Link<S> qsort( final Link<S> list ) {
        final Link<S> result;

        if (list == null || list.tail==null) {
            result = list;
        } else {
            final Pair<Link<S>, Link<S>> pair = partition( list.head, list.tail );  // leq is stored as Object1, gt is stored as Object2 in pair
            final Link<S> leqSorted = qsort( pair.getObject1() );
            final Link<S> gtSorted = qsort( pair.getObject2() );
            list.tail = gtSorted;
            result = append( leqSorted, list );
        }
        return result;
    }

    public static <S extends Comparable<S>> Pair<Link<S>,Link<S>> partition( final S pivot, final Link<S> list ) {
        PartitionTraverser<S> partitiontraverser = new PartitionTraverser<S>( pivot , list );   // The Task is instantiated and called inside PartitionTraverser
        return partitiontraverser.getPartitionPair();
    }

    public Link nextLink() {
        Link nextLink = this.tail;

        return nextLink;
    }

    public static <S extends Comparable<S>> Link<S> append( final Link<S> start, final Link<S> end ) {
        final Link<S> result;

        if (start == null) {
            result = end;
        } else if (end == null) {
            result = start;
        } else {
            result = start;
            Link<S> current = start;
            Traverser<Link<S>> traverser = new Traverser<Link<S>>( current );
            Task<Link<S>> appendtask = new AppendTask<S>( end );    // appends end to the last Link in the chain
            traverser.traverse( appendtask );
        }
        return result;
    }

    // Iterates the values of the Links
    public static <T> Iterator<T> iterator( final Link<T> link ) {

        return new Iterator<T>() {
            private Link<T> current = link;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public T next() {
                final T next = current.head;
                current = current.tail;
                return next;
            }
        };
    }

    // Iterates the Links in the chain
    @Override
    public Iterator<Link<T>> iterator( ) {
        Link<T> current_link = this;

        return new Iterator<Link<T>>() {
            private Link<T> current = current_link;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public Link<T> next() {
                final Link<T> next = current;
                current = current.tail;
                return next;
            }
        };
    }
}