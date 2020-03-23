/**
* the superclass to all lights
*/
public interface Light extends Component {
    final String LABEL = "light";
    String state = "off";

    public void turnOn();

    public void turnOff();
}
