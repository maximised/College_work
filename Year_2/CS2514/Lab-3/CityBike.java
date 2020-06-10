/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

import java.util.*;
import java.lang.*;

public final class CityBike implements Bike {

    private FrontLight frontlight = new FrontLight();
    private RearLight rearlight = new RearLight();;
    private Carrier carrier = new Carrier();
    private HighFrame highframe = new HighFrame();
    private final String LABEL = "city bike";

    private ConcreteBike citybike = new ConcreteBike( LABEL, highframe );


    public CityBike() {
        this.citybike.add_component( frontlight );
        this.citybike.add_component( rearlight );
        this.citybike.add_component( carrier );
    }

    @Override
    public void print() {
        citybike.print();
    }

    @Override
    public void println() {
        citybike.println();
    }

    @Override
    public Iterator<Component> iterator() {
        final ArrayList<Component> component_list = citybike.get_components();
        return new Iterator<Component>() {
            int position = 0;

            @Override
            public boolean hasNext() {
                return position != component_list.size();
            }

            @Override
            public Component next() {
                return component_list.get( position++ );
            }
        };
    }
}



