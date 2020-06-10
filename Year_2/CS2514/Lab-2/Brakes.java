/**
 * inherits from the components class to create the brakes of a bike
 */
public class Brakes extends Component {
    final private String LABEL = "brakes";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.LABEL;
    }
}
