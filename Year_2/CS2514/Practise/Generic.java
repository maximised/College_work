public class Generic {
    public static <E> void printStuff(E[] arr) {
        for(E element: arr) {
            System.out.println(element);
        }
        System.out.println();
    }

    public static void main(String args[]) {
        Integer[] intArray = {1,2,3,4};

        printStuff(intArray);
    }
}