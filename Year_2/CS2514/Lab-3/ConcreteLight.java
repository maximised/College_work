/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class ConcreteLight implements Light {
	final private String LABEL;
    private String state;
    private ConcreteComponent light;

    public ConcreteLight( String LABEL, String state ) {
    	this.LABEL = LABEL;
    	this.state = state;

    	light = new ConcreteComponent( LABEL, state );
    }

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
        light.print();
    }
}