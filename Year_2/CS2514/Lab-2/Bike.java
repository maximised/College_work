/**
 * The superclass of all bikes and contains the shared components of all bikes
 *
 * @author: MAXIM CHOPIVSKYY (118364841)
 */
public class Bike {
    private Brakes brakes;
    private Saddle saddle;
    private Wheels wheels;
    private Handlebar handlebar;
    private final String LABEL = "bike";

    /**
    * This prints all the shared components of all bikes
    */
    void printComponents(){
        System.out.println("The components of a " + this + " are:");
        System.out.println(brakes);
        System.out.println(wheels);
        System.out.println(saddle);
        System.out.println(handlebar);
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
    * This is the constructor to create a Bike with the shared components
    */
    public Bike ( ){
        this.brakes = new Brakes();
        this.wheels = new Wheels();
        this.saddle = new Saddle();
        this.handlebar = new Handlebar();
    }
}
