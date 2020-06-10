public interface Subject<E,U> {
    public void attach( final Observer<U> observer );
    public void detach( final Observer<U> observer );
    public void notify( final E event );
}
