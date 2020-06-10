/**
 * Question 4: Linked Lists. 
 * The Link of the List class
 *
 * @author: (118364841)
 */

 /**
* This is the Task of the append() funtion in the Link class.
* This appends the end of the chain of Link elements.
*/
public class AppendTask<T> implements Task<Link<T>> {

    private final Link<T> end;

    /**
    * This constructor sets the end Link
    * @param end will be added to the end of the chain
    */
    public AppendTask( final Link<T> end ) {
        this.end = end;
    }

    /**
    * appends to the Link the paramter object.
    * @param object is the Link we append if its at the end
    */    
    @Override
    public void apply( final Link<T> object ) {
        if ( object.nextLink()==null ) {
            object.setTail( end );
        }
    }
}