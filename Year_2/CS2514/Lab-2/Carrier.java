/**
 * inherits from the components class to create the carrier of a bike
 */
public class Carrier extends Component {
    final private String LABEL = "carrier";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.LABEL;
    }
}
