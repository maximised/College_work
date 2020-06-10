/**
 * Question 3: Interfaces.
 *
 * @author: (118364841)
 */

 /**
∗ Generic interface for collections which allows for a traversal
∗ of the members of the collection and applying a task to each member
∗ of the collection.
*/
public interface Traversable<T> extends Iterable<T> {
    /**
    ∗ Apply a task to each member of this <code> Iterable </code> collection.
    * @param task The task which is applied to each individual
    * member of this <code> Iterable </code> collection.
    */
    public void traverse( final Task<T> task );
}