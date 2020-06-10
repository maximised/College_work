public class Tally {
    private static int creations;
    private int number;
    private int counter;

    public static void main( final String[] args ) {
        final Tally t1 = new Tally( );
        final Tally t2 = new Tally( );
        t1.increment( );
        t1.increment( );
        t2.increment( );
        System.out.println( t1.toString( ) );
        System.out.println( t2.toString( ) );
    }

    public Tally( ) {
        number = ++ creations;
        counter = 0;
    }

    public void increment( ) {
        counter = counter + 1;
    }

    @Override
    public String toString( ) {
        return "Tally[ number = " + number
                   + ", counter = " + counter + " ]";
    }
}
