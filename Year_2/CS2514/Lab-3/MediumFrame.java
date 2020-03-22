/**
 * inherits from the Frame class to create the medium frame of a bike
 */
public final class MediumFrame implements Frame {
    final private String LABEL = "medium frame";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.LABEL;
    }
}
