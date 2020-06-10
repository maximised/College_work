/**
 * inherits from the Frame class to create the high frame of a bike
 */
public class HighFrame extends Frame {
    final private String LABEL = "high frame";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.LABEL;
    }
}
