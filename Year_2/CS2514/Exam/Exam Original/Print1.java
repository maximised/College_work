public class Print1<T> implements Task<Link<T>> {

	@Override
	public void apply( final Link<T> object ) {
		System.out.println( object.getHead() );
	}
}