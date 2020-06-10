/**
 * Question 4: Linked Lists. 
 * The Link of the List class
 *
 * @author: (118364841)
 */

import java.util.Iterator;

/**
* This class is used to implement in the quicksort algorithm, by traversing through the Link elements and applying a Task to each.
* The Task is an inner class of this class.
*/
public class PartitionTraverser<S extends Comparable<S>> implements Traversable<Link<S>> {
    private final Link<S> leq; // members less than or equal to the pivot.
    private final Link<S> gt;  // members greater than the pivot.
    private final Link<S> link;
    private final S pivot;

    /**
    ∗ Constructs the Traversable object with its pivot and link to partition.
    * It creates a Task instance and applies the Task apply method to each element in the Link object.
    * The greater and less_or_equal partitions are created from the Traverse of the Task, and are stored in this class reference.
    * @param pivot The pivot of the current step in the quicksort algorithm
    * each of its elements.
    */
    public PartitionTraverser( final S pivot, final Link<S> list ) {
        this.link = list;
        this.pivot = pivot;

        final PartitionTask<S> partitiontask = new PartitionTask<S>( pivot );
        this.traverse( partitiontask );

        this.gt = partitiontask.gt;
        this.leq = partitiontask.leq;
    }

    /**
    * Returns the leq and gt calculated from the Traversal. Is used after we Traverse and Partition the List.
    * @return The pair leq and gt as a Pair object
    */
    public Pair<Link<S>, Link<S>> getPartitionPair( ) {
        Pair<Link<S>, Link<S>> pair = new Pair<Link<S>, Link<S>>( this.leq, this.gt );
        return pair;
    }

    /**
    ∗ Apply a task to each member of this <code> Iterable </code> collection.
    * @param task The task which is applied to each individual
    * member of this <code> Iterable </code> collection.
    */
    @Override
    public void traverse( final Task<Link<S>> task ) {
        Link<S> leq = null;
        Link<S> gt = null;

        for (Link<S> object : this) {
            task.apply( object );
        }   
    }

    /**
    ∗ Lets you iterate through the link attribute.
    * @return the iterator of the link.
    */
    @Override
    public Iterator<Link<S>> iterator() {
        return link.iterator();
    }

    //############################################################################################################################

    /**
    * This is the Task of the PartitionTraverser class and its inner class.
    * This is used to apply a task to each Link element passed to it, and create the Partition.
    */
    private class PartitionTask<S extends Comparable<S>> implements Task<Link<S>> {

        private final S pivot;
        Link<S> gt;
        Link<S> leq;
        // still respects encapsulation because it's in private inner class

        /**
        * This constructs the PartitonTask. gt and leq start as null and as we Traverse through the Link, elements are added to them.
        * @param pivot is the pivot passed in from the outer class.
        */
        private PartitionTask( final S pivot ) {
            this.pivot = pivot;
            gt = null;
            leq = null;
        }

        @Override
        public void apply( final Link<S> object ) {
            if (object.getHead().compareTo( pivot ) > 0) {
                object.setTail( gt );
                //Link<S> item = new Link<S>(object, gt);
                gt = object;//item
            } else {
                object.setTail( leq );
                //Link<S> item = new Link<S>(object, leq);
                leq = object; //item
            }
        }

    }

//
}