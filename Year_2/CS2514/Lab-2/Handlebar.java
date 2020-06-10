/**
 * inherits from the components class to create the handlebar of a bike
 */
public class Handlebar extends Component {
    private String LABEL = "handlebar";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component
    */
    @Override
    public String toString( ) {
        return this.LABEL;
    }
}

