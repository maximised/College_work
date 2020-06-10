/**
 * This is the superclass to all bike components
 *
 * @author: MAXIM CHOPIVSKYY (118364841)
 */
public class Component {
    final private String LABEL = "component";

    /**
     * this method prints the type of component it is
     * @return String is the type of component
     */
    @Override
    public String toString( ) {
        return this.LABEL;
    }
}

