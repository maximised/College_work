public class Reader implements Observer<String> {
    private final String name;

    public Reader( final String name ) {
        this.name = name;
    }

    @Override
    public void update( final String information ) {
       System.out.println( name + " receiving " + information );
    }
}
