/**
 * Question 2: A Generic Pair Class
 * 
 * @author: (118364841)
 */
public class Pair<T, U> {
    private T object1;
    private U object2;

    public Pair() {
        object1 = null;
        object2 = null;
    }

    public Pair( final T o1, final U o2 ) {
        this.object1 = o1;
        this.object2 = o2;
    }

    public T getObject1() {
        return object1;
    }

    public void setObject1( final T newObject1 ) {
        object1 = newObject1;
    }

    public U getObject2() {
        return object2;
    }

    public void setObject2( final U newObject2 ) {
        object2 = newObject2;
    }

    @Override
    public boolean equals( Object obj ) {
        if ( obj == null ) {
            return false;
        }

        if ( !Pair.class.isAssignableFrom(obj.getClass()) ) {
            return false;
        }

        final Pair other = (Pair) obj;
        if ( other.getObject1()==object1 & other.getObject2()==object2 ) {
            return true;
        } else {
            return false;
        }
    }

    @Override
    public String toString() {
        return "Object reference 1 is: " + object1 + "\nObject reference 2 is: " + object2;
    }
} 