/**
 * Inherits from the Bike class and adds components for the Mountain Bike
 *
 * @author: MAXIM CHOPIVSKYY (118364841)
 */
public class MountainBike extends Bike {
    private LowFrame lowframe;
    private final String LABEL = "mountain bike";

    /**
    * This is the constructor to create a Mountain Bike
    */
    public MountainBike() {
        super();
        this.lowframe = new LowFrame();     
    }

    /**
    * allows to print the name of the bike class
    * @return String is the name of bike
    */
    @Override
    public String toString() {
        return this.LABEL;
    }

    /**
    * This prints all the components of the Mountain Bike including the shared components every
    * bike has
    */
    @Override
    void printComponents() {
        super.printComponents();
        System.out.println(lowframe);
        System.out.println();
    }
}

