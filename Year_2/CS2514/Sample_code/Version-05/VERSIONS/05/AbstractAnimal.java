public final class AbstractAnimal implements Animal {
    private final boolean eatsMeat;
    private final String species;

    public AbstractAnimal( final boolean eatsMeat, final String species ) {
        this.eatsMeat = eatsMeat;
        this.species = species;
    }

    @Override
    public String getFood( ) {
        return eatsMeat ? "meat" : "grass";
    }

    @Override
    public String getSpecies( ) {
        return species;
    }

    @Override
    public void eat( ) {
        System.out.println( getSpecies( ) + " eating " + getFood( ) );
    }
}
