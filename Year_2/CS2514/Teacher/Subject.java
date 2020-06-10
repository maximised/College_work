public interface Subject<U, V> {
	public void attach( final Observer<U> student);
	public void detach( final Observer<U> student);
	public void notify ( final V announcement );
}