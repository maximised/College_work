import java.util.Scanner;

/**
 * Program for reading lotto numbers and returning prize
 *
 * @author: MAXIM CHOPIVSKYY (118364841)
 */
public class Ticket {
    
    final Integer[] winning_nums = new Integer[]{1,4,6,7,21,30};
    static Integer[] chosen_nums = new Integer[6];

    /**
     * This class method reads in numbers from the user and returns their lotto numbers
     *
     * @author: MAXIM CHOPIVSKYY (118364841)
     */
    public static Integer[] readTicketNumbers(){
        Scanner scanner = new Scanner(System.in);

        int i = 0;
        int num;
        System.out.println("Type the lotto numbers one at a time");
        while(i < 6){
            num = scanner.nextInt();
            if (num < 1 || num > 42){
                System.out.println("Invalid number. Try again.");
            }
            else{
                chosen_nums[i] = num;
                i += 1;
            }
        }
        return chosen_nums;
    }

    /**
     * This instance method prints out the numbers on the ticket.
     */
    public void printNumbers(){
        System.out.printf("Your lotto numbers are: ");
        for(Integer i: chosen_nums){
            System.out.printf("%d ", i.intValue());
        }
        System.out.println();
    }

    /**
     * This instance method prints the amount of prize money the ticket would win
     */
    public void printPrizeMoney(){
        int c = 0;
        int prize = 0;
        for (int i = 0; i<6; i++){
            for (int j=0; j<6; j++){
                if(chosen_nums[i].intValue() == winning_nums[j].intValue()){
                    c += 1;
                    break;
                }
            }
        }
        switch(c){
            case 3: prize=3;
            break;

            case 4: prize=30;
            break;

            case 5: prize=30000;
            break;

            case 6: prize=1000000;
            break;
        }

        System.out.printf("The prize money is: %d\n", prize);
    }

    public Ticket( Integer[] nums ){
        chosen_nums = nums;
    }
    
    /**
     * This is the main method which uses all the other methods to read in numbers for a 
     *ticket and print the prize money for that ticket
     */
    public static void main( String[] args ){
        Ticket t1 = new Ticket( readTicketNumbers() );
        
        t1.printNumbers();
        t1.printPrizeMoney();

    }
    
}
