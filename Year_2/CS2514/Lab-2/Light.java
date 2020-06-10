/**
* the superclass to all lights
*/
public class Light extends Component {
    final private String LABEL = "light";
    private String state = "off";

    /**
    * lets us turn on the light
    */
    public void turnOn() {
        this.state = "on";
    }

    /**
    * lets us turn off the light
    */
    public void turnOff() {
        this.state = "off";
    }

    /**
    * allows us to print what type of component this is
    * @return String is the type of component and whether its on or off
    */
    @Override
    public String toString() {
        return this.LABEL + ": " + this.state;
    }
}
