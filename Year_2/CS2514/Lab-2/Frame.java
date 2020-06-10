/**
 * inherits from the Component class to create the frame of a bike
 */
public class Frame extends Component {
    final private String LABEL = "frame";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.LABEL;
    }
}
