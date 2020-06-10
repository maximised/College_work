public abstract class Carnivore extends Animal {
    public Carnivore( final String species ) {
        super( true, species );
    }

    @Override
    public void eat( ) {
        System.out.println( getSpecies( ) + " eating MEAT" );
    }
}
