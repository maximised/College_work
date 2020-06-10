public final class Dog implements Carnivore {
    private final Carnivore carnivore;

    public Dog( ) {
        carnivore = new ConcreteCarnivore( "dog" );
    }

    @Override
    public String getFood( ) {
        return carnivore.getFood( );
    }

    @Override
    public String getSpecies( ) {
        return carnivore.getSpecies( );
    }

    @Override
    public void eat( ) {
        carnivore.eat( );
    }
}
