/**
 * inherits from the components class to create the rear light of a bike
 */
public final class RearLight implements Light {
    final private String LABEL = "rear light";
    private String state = "off";

    /**
    * allows us to print what type of component this is
    * @return String is the type of component and whether its on or off
    */
    @Override
    public String toString() {
        return this.LABEL + ": " +  this.state;
    }

    /**
    * lets us turn on the light
    */
    @Override
    public void turnOn() {
        this.state = "on";
    }

    /**
    * lets us turn off the light
    */
    @Override
    public void turnOff() {
        this.state = "off";
    }
}
