/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class FrontLight implements Light {
    final private String LABEL = "front light";
    private String state = "off";
       
    ConcreteLight frontlight = new ConcreteLight( LABEL, state );


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
        frontlight.print();
    }
}
