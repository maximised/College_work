/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

import java.util.*;
import java.lang.*;

public final class MountainBike implements Bike {
    private LowFrame lowframe = new LowFrame();
    private final String LABEL = "mountain bike";

    private ConcreteBike mountainbike = new ConcreteBike( LABEL, lowframe );


    public MountainBike() {
    }

    @Override
    public void print() {
        mountainbike.print();
    }

    @Override
    public void println() {
        mountainbike.println();
    }

    @Override
    public Iterator<Component> iterator() {
        final ArrayList<Component> component_list = mountainbike.get_components();
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

