/**
 * Question 3: Interfaces. 
 *
 * @author: (118364841)
 */
import java.util.*;

/**
∗ Generic class which implements the Generic Traversable class. 
* This is for collections which allows for a traversal of the members of the collection and applying a task to each member
∗ of the collection using a Task object.
*/
public class Traverser<T> implements Traversable<T> {
    private final Iterable<T> list;

    /**
    ∗ Constructs the Traversable object to set an iterable object as its one attribute.
    * @param iterable_object The iterable object we will traverse and apply tasks to
    * each of its elements.
    */
    public Traverser( final Iterable<T> iterable_object ) {
        list = iterable_object;
    }

    /**
    ∗ Apply a task to each member of this <code> Iterable </code> collection.
    * @param task The task which is applied to each individual
    * member of this <code> Iterable </code> collection.
    */
    @Override
    public void traverse( final Task<T> task ) {
        for (T item : this) {
            task.apply( item );
        }
    }

    /**
    ∗ Lets you iterate through the list attribute.
    * @return the iterator of the list.
    */
    @Override
    public Iterator<T> iterator() {
        return list.iterator();
    }
}