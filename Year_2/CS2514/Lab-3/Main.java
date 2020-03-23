/**
 * The main class which prints out each type of bike
 *
 * @author: MAXIM CHOPIVSKYY (118364841)
 */
public final class Main {


    /**
     * this method creates each type of bike and prints them out
     * @param args Unused.
     */
     public static void main( String[] args){
     Bike cityBike = new CityBike();
     cityBike.print();

     Bike mountainBike = new MountainBike();
     mountainBike.print();

     Bike hybridBike = new Hybrid();
     hybridBike.print();
     }
}
