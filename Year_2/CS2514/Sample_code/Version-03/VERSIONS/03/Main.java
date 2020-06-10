public class Main {
    public static void main( String[] args ) {
        final Paper paper = new Paper( "Echo" );
        final Reader john = new Reader( "John" );
        final Reader carl = new Reader( "Carl" );
        paper.attach( john );
        paper.attach( carl );
        paper.notify( 9 );
    }
}
