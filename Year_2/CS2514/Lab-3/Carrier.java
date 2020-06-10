/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class Carrier implements Component{
    final private String LABEL = "carrier";
    private ConcreteComponent carrier = new ConcreteComponent( LABEL );

    public void print( ) {
        carrier.print();
    }
}
