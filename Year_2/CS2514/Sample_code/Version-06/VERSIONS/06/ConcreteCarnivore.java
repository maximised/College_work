public final class ConcreteCarnivore implements Carnivore {
    private final Animal animal;

    public ConcreteCarnivore( final String species ) {
        animal = new ConcreteAnimal( true, species );
    }

    @Override
    public String getFood( ) {
        return animal.getFood( );
    }

    @Override
    public String getSpecies( ) {
        return animal.getSpecies( );
    }

    @Override
    public void eat( ) {
        animal.eat( );
    }
}
