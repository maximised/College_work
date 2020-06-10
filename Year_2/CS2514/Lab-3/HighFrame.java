/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class HighFrame implements Frame {
    final private String LABEL = "high frame";
    private ConcreteComponent highframe = new ConcreteComponent( LABEL );


    @Override
    public void print( ) {
        highframe.print();
    }
}
