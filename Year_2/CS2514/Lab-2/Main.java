/**
 * The main class which prints out each type of bike
 *
 * @author: MAXIM CHOPIVSKYY (118364841)
 */
public class Main {


    /**
     * this method creates each type of bike and prints them out
     * @param args Unused.
     */
     public static void main( String[] args){
     Bike cityBike = new CityBike();
     cityBike.printComponents();

     Bike mountainBike = new MountainBike();
     mountainBike.printComponents();

     Bike hybridBike = new Hybrid();
     hybridBike.printComponents();
     }
}
