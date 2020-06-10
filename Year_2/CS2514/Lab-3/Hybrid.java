/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

import java.util.*;
import java.lang.*;

public final class Hybrid implements Bike {
    private FrontLight frontlight = new FrontLight();
    private RearLight rearlight = new RearLight();
    private MediumFrame mediumframe = new MediumFrame();;
    private final String LABEL = "hybrid";

    private ConcreteBike hybrid = new ConcreteBike( LABEL, mediumframe );

    public Hybrid() {
         this.hybrid.add_component( frontlight );
         this.hybrid.add_component( rearlight );
    }

    @Override
    public void print() {
        hybrid.print();
    }

    @Override
    public void println() {
        hybrid.println();
    }

    @Override
    public Iterator<Component> iterator() {
        final ArrayList<Component> component_list = hybrid.get_components();
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

