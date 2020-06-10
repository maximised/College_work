/**
 * Question 3: Interfaces.
 *
 * @author: (118364841)
 */

/**
∗ Generic interface which defines an <code> apply </code> method
∗ which applies a task to its argument.
*/
public interface Task<T> {
    /**
    ∗ Apply this instance’s task to an object argument.
    * @param object The object to which this task is applied.
    */
    public void apply( final T object );
}