/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class RearLight implements Light {
    final private String LABEL = "rear light";
    private String state = "off";
       
    private ConcreteLight rearlight = new ConcreteLight( LABEL, state );


    @Override
    public void turnOn() {
        this.state = "on";
    }

    @Override
    public void turnOff() {
        this.state = "off";
    }

    @Override
    public void print( ) {
        rearlight.print();
    }
}
