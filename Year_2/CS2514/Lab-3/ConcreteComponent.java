/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class ConcreteComponent implements Component {
    private final String LABEL;
    private String state;

    public ConcreteComponent( final String LABEL ) {
        this.LABEL = LABEL;
    }

    public ConcreteComponent( final String LABEL, String state ) {
        this.LABEL = LABEL;
        this.state = state;
    }

    @Override
    public void print( ) {
        if (state != null) {
            System.out.print( LABEL + ": " + state );
        }
        else {
            System.out.print( LABEL );
        }
    }
}