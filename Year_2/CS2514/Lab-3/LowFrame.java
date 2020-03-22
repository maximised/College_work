/**
 * inherits from the frame class to create the low frame of a bike
 */
public final class LowFrame implements Frame {
    final private String LABEL = "low frame";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.LABEL;
    }
}
