/**
* the superclass to all lights
*/
public interface Light implements Component {
    final private String LABEL = "light";
    private String state = "off";

    public void turnOn();

    public void turnOff();
}
