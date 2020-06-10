/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class MediumFrame implements Frame {
    final private String LABEL = "medium frame";
    private ConcreteComponent mediumframe = new ConcreteComponent( LABEL );

    @Override
    public void print( ) {
        mediumframe.print();
    }
}
