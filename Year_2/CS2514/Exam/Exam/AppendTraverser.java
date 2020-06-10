import java.util.Iterator;

/**
 * Question 4: Linked Lists. 
 * The Link of the List class
 *
 * @author: (118364841)
 */

/**
* This is the Traverser of the append() funtion in the Link class.
* This appends the end of the chain of Link elements.
*/
public class AppendTraverser<T> implements Traversable<Link<T>> {

    private final Link<T> list;

    /**
    ∗ Constructs the object to set a Link object as its one attribute.
    * @param link_object The object we will traverse and apply tasks to
    * each of its elements.
    */
    public AppendTraverser( final Link<T> link_object ) {
        this.list = link_object;
    }

    /**
    ∗ Apply a task to each member of this <code> Iterable </code> collection.
    * @param task The task which is applied to each individual
    * member of this <code> Iterable </code> collection.
    * There is an if statement so we apply it to the last link.
    */
    @Override
    public void traverse( final Task<Link<T>> task ) {
        for (Link<T> item : this) {
            if (item.nextLink() == null) {
                task.apply( item );
            }
        }
    }

    /**
    ∗ Lets you iterate through the list attribute.
    * @return the iterator of the list.
    */
    @Override
    public Iterator<Link<T>> iterator() {
        return list.iterator();
    }
}