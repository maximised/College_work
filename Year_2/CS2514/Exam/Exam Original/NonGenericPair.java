/**
 * Question 1: A Non-Generic Pair Class
 *
 * @author: (118364841)
 */

public class NonGenericPair {
    private Object object1;
    private Object object2;

    /**
    * The construcor with no parameters gives the pair of references default null values
    * This is if user doesn't choose values for the pair
    */
    public NonGenericPair() {
        object1 = null;
        object2 = null;
    }

    /**
    * This constructor sets the references to chosen values in parameter
    * @param object1 is assigned to the first object reference
    * @param object2 is assigned to the second object reference
    */
    public NonGenericPair( final Object object1, final Object object2 ) {
        this.object1 = object1;
        this.object2 = object2;
    }

    /**
    * @return the first object reference
    */
    public Object getObject1() {
        return object1;
    }

    /**
    * @param newObject1 the newly assigned object to first object reference
    */
    public void setObject1( final Object newObject1 ) {
        object1 = newObject1;
    }

    /**
    * @return the second object reference
    */
    public Object getObject2() {
        return object2;
    }

    /**
    * @param newObject2 the newly assigned object to second object reference
    */
    public void setObject2( final Object newObject2 ) {
        object2 = newObject2;
    }

    /**
    * checks if the pair of this instance has same pair as NonGenericPair other object
    * @param obj is the other object to be compared with this instance
    * @return boolean is true if they are equal and false if not
    */
    @Override
    public boolean equals( Object obj ) {
        if (obj == null) {
            return false;
        }

        if (!NonGenericPair.class.isAssignableFrom(obj.getClass())) {
            return false;
        }

        final NonGenericPair other = (NonGenericPair) obj;
        if ( other.getObject1()==object1 & other.getObject2()==object2 ) {
            return true;
        } else {
            return false;
        }
    }

    /**
    * allows to turn the Pair into a String showing the two references
    * @return String shows the two object references in the instance
    */
    @Override
    public String toString() {
        return "Object reference 1 is: " + object1 + "\nObject reference 2 is: " + object2;
    }
} 