/**
 * inherits from the components class to create the saddle of a bike
 */
public class Saddle extends Component {
    private String label = "saddle";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.label;
    }
}
