public final class AbstractCarnivore implements Carnivore {
    private final Animal animal;

    public AbstractCarnivore( final String species ) {
        animal = new AbstractAnimal( true, species );
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
