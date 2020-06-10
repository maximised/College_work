import java.util.*;

public class Booleans implements Iterable<Boolean> {
    public static void main( final String[] args ) {
        final Booleans booleans = new Booleans( );

        final Iterator<Boolean> iterator = booleans.iterator( );
        while (iterator.hasNext( )) {
            final Boolean b = iterator.next( );
            System.out.println( b );
        }
    }

    @Override
    public Iterator<Boolean> iterator( ) {
        return new Iterator<Boolean>( ) {
            private TriState state = TriState.values( )[ 0 ];

            @Override
            public boolean hasNext( ) {
                final TriState[] values = TriState.values( );
                return state != values[ values.length - 1 ];
            }

            @Override
            public Boolean next( ) {
                final TriState[] values = TriState.values( );
                final Boolean result;

                result = (state.ordinal( ) == 0) ? Boolean.FALSE : Boolean.TRUE;
                state = values[ state.ordinal( ) + 1 ];

                return result;
            }
        };
    }
    private enum TriState {
        INITIAL, INTERMEDIATE, FINAL;
    }

}
