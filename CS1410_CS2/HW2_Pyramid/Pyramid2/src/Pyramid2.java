import java.util.Scanner;
import java.lang.Math;


public class Pyramid2 {
    //Pyramid2 makes a pyramid with middle descending number increasing by power of two.
    public static void main(String[] args) {
        //getting input from the user
        System.out.printf("Input the number of pyramid lines: ");
        Scanner input = new Scanner(System.in);
        String userNum = input.nextLine();

        //figuring how many digits are in the largest number that will be printed
        int numRows = Integer.parseInt(userNum);  //number or rows requested by user
        double maxWidth = Math.pow(2,numRows);  //biggest number that will be printed
        int digit = (int)maxWidth;
        int lengthOfDigit = String.valueOf(digit).length(); //number of digits in largest number

        //Outer for loop counts the line the program is on
        for (int currentLine = 1; currentLine <= numRows; currentLine++) {

            //first for loop adds correct white space to shift column
            for (int blankCount = numRows - currentLine; blankCount >= 1; blankCount-- ) {
                String blank = " %" + lengthOfDigit +"s";
                System.out.printf(blank,"");
            }

            //second for loop creates all increasing numbers including largest middle number
            for (int increment = 0; increment < currentLine; increment++) {
                double growth = Math.pow(2,increment);  //the number in each line increases by 2 the power of the next place
                int value = (int) growth;
                String format = " %" + lengthOfDigit + "s";
                System.out.printf(format, value);
            }

            //third for loop creates all descending numbers except for largest middle number. Adjusting the starting
            //place for the loop allowed for the loop to start on the second line and begin with the second smallest number
            for (int decrement = currentLine+1; decrement > 2; decrement--) {
                double shrink = Math.pow(2,(decrement-3));
                int value = (int) shrink;
                String format = " %" + lengthOfDigit + "s";
                System.out.printf(format, value);
            }

            //to create a new blank line every iteration
            System.out.println("");

        }

    }

}
