public class MyArray implements MyIterable {
    private final Object[] values;
    private int size;

    public static void main( final String[] args ) {
        final MyArray values = new MyArray( 3 );
        values.add( 2 );
        values.add( 0 );
        values.add( 1 );
        final MyIterator iterator = values.iterator( );
        while (iterator.hasNext( )) {
            final Object object = iterator.next( );
            System.out.println( object );
        }
    }

    public MyArray( final int capacity ) {
        values = new Object[ capacity ];
        size = 0;
    }

    public void add( final Object object ) {
        values[ size++ ] = object;
    }

    @Override
    public MyIterator iterator( ) {
        return new MyIterator( ) {
            private int position = 0;
            @Override
            public boolean hasNext( ) {
                return position != size;
            }
            @Override
            public Object next( ) {
                return values[ position++ ];
            }
        };
    }
}
