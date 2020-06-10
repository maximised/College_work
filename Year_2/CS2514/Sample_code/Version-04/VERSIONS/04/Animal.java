public abstract class Animal {
    private final boolean eatsMeat;
    private final String species;

    public Animal( final boolean eatsMeat, final String species ) {
        this.eatsMeat = eatsMeat;
        this.species = species;
    }

    private String getFood( ) {
        return eatsMeat ? "meat" : "grass";
    }

    public String getSpecies( ) {
        return species;
    }

    public abstract void eat( );
}
