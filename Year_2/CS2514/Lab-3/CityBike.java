/**
 * Inherits from the Bike class and adds components for the City Bike
 *
 * @author: MAXIM CHOPIVSKYY (118364841)
 */
public final class CityBike implements Bike {
    private FrontLight frontlight;
    private RearLight rearlight;
    private Carrier carrier;
    private HighFrame highframe;
    private final String LABEL = "city bike";

    /**
    * This is the constructor to create a City Bike
    */
    public CityBike() {
        super();
        this.frontlight = new FrontLight();
        this.rearlight =  new RearLight();
        this.carrier = new Carrier();
        this.highframe = new HighFrame();    
    }

    /**
    * allows to print the name of the bike class
    * @return String is the type of bike
    */
    public String toString() {
        return this.LABEL;
    }

    /**
    * This prints all the components of the City Bike including the shared components every
    * bike has
    */
    @Override
    void print() {
        super.printComponents();
        System.out.println(frontlight);
        System.out.println(rearlight);
        System.out.println(carrier);
        System.out.println(highframe);
        System.out.println();
    }

    @Override
    void println() {
        super.printComponents();
        System.out.println(frontlight);
        System.out.println(rearlight);
        System.out.println(carrier);
        System.out.println(highframe);
        System.out.println();
    }
}



