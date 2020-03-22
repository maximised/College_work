/**
 * Inherits from the Bike class and adds components for the Hybrid Bike
 *
 * @author: MAXIM CHOPIVSKYY (118364841)
 */
public final class Hybrid implements Bike {
    private FrontLight frontlight;
    private RearLight rearlight;
    private MediumFrame mediumframe;
    private final String LABEL = "hybrid";

    /**
    * This is the constructor to create a Hybrid Bike
    */
    public Hybrid() {
         super();
         this.frontlight = new FrontLight();
         this.rearlight = new RearLight();
         this.mediumframe = new MediumFrame();
    }

    /**
    * allows to print the name of the bike class
    * @return String is the type of bike
    */
    @Override
    public String toString() {
        return this.LABEL;
    }

    /**
    * This prints all the components of the Hybrid Bike including the shared components every
    * bike has
    */
    @Override
    void print() {
        super.printComponents();
        System.out.println(frontlight);
        System.out.println(rearlight);
        System.out.println(mediumframe);
        System.out.println();
    }
}

