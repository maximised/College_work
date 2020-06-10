/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class LowFrame implements Frame {
    final private String LABEL = "low frame";
    private ConcreteComponent lowframe = new ConcreteComponent( LABEL );

    @Override
    public void print( ) {
        lowframe.print();
    }
}
