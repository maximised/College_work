import java.util.*;

public class Paper implements Subject<Integer,String> {
    private final List<Observer<String>> observers;
    private final String name;

    public Paper( final String name ) {
        this.name = name;
        observers = new ArrayList<Observer<String>>( );
    }

    @Override
    public void attach( final Observer<String> observer ) {
        observers.add( observer );
    }

    @Override
    public void detach( final Observer<String> observer ) {
        observers.remove( observer );
    }

    private String edit( final Integer event ) {
        return "New event #" + event;
    }

    @Override
    public void notify( final Integer event ) {
        System.out.println( "Paper " + name + " receiving news" );
        final String news = edit( event );
        for( Observer observer : observers ) {
            observer.update( news );
        }
    }
}
