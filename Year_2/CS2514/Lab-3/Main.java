/**
 * @author: MAXIM CHOPIVSKYY (118364841)
 */

public final class Main {

     public static void main( String[] args) { 

          System.out.println( "Printing hybrid now:" );
          final Hybrid hybrid = new Hybrid();
          System.out.println( "print function:" );
          hybrid.print();
          System.out.println( "println function:" );
          hybrid.println();
          System.out.println( "for loop:" );
          for ( Component component : hybrid) {
               component.print();
               System.out.print( ", " );
          }

          System.out.println();
          System.out.println();

          System.out.println( "Printing mountainbike now:" );
          final MountainBike mountainbike = new MountainBike();
          System.out.println( "print function:" );
          mountainbike.print();
          System.out.println( "println function:" );
          mountainbike.println();
          System.out.println( "for loop:" );
          for ( Component component : hybrid) {
               component.print();
               System.out.print( ", " );
          }

          System.out.println();
          System.out.println();

          System.out.println( "Printing citybike now:" );
          final CityBike citybike = new CityBike();
          System.out.println( "print function:" );
          citybike.print();
          System.out.println( "println function:" );
          citybike.println();
          System.out.println( "for loop:" );
          for ( Component component : hybrid) {
               component.print();
               System.out.print( ", " );
          }
          

     }
}
