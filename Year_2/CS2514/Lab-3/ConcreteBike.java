/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

import java.util.*;
import java.lang.*;

public final class ConcreteBike implements Bike {
	private final String NAME;
	private final Frame frame;
	private ArrayList<Component> component_list  = new ArrayList<Component>();

	public ConcreteBike( final String NAME, Frame t ) {
		this.NAME = NAME;
		this.frame = t;
		component_list.add(this.frame);
	}

    public void add_component( Component component ) {
        this.component_list.add( component );
    }


	@Override
	public void print() {
        for ( Component component : this ) {
            component.print();
            System.out.print( ", " );
        }    
	}

	@Override
	public void println() {
        for ( Component component : this ) {
            component.print();
            System.out.println();
        }
	}

    public ArrayList<Component> get_components() {
        return this.component_list;
    }


	@Override
	public Iterator<Component> iterator() {
		final ArrayList<Component> component_list = this.component_list;
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