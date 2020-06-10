/**
 * inherits from the components class to create the wheels of a bike
 */
public class Wheels extends Component {
    private String label = "wheels";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.label;
    }
}
