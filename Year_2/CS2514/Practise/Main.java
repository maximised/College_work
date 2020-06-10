import java.util.*;

public class Main {
	public static void main(String args[]) {
		Generic generic = new Generic();
		Integer[] intArray = {1,2,3,4};

        generic.printStuff(intArray);


        /*
        Compare<Integer> compare1;
        compare1 = new Compare<Integer>(5);
        Compare<Integer> compare2; 
        compare2 = new Compare<Integer>(6);

        System.out.println(compare1);
        */

        //compare1.compareTo(compare2);

        //Comparable list = 
        Integer[] list = {4,7,3,7};

        Binsearch bin = new Binsearch( 3, list, 0, 3);

	}
}