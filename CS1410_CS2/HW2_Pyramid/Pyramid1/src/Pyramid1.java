import java.util.Scanner;

public class Pyramid1 {
    //Pyramid1 creates a pyramid beginning with the line number on the outside,
    //decreasing to 1 in the middle then increasing back to the line number on the outside
    public static void main(String[] args) {
        //Asking the user for the number of pyramid lines and figuring out how many digits are in said number.
        System.out.print("Input the number of pyramid lines: ");
        Scanner input = new Scanner(System.in);
        String userNum = input.nextLine();
        int numColumn = Integer.parseInt(userNum);
        int lengthOfDigit = String.valueOf(userNum).length();
        int columWidth = lengthOfDigit + 1;

        //outer for loop counts the pyramid line
        for (int currentLine = 1; currentLine <= numColumn; currentLine++) {

            //first for loop adds white space to center the pyramid from the left
            for (int blankCount = numColumn - currentLine; blankCount >= 1; blankCount-- ) {
                String blank = " %" + lengthOfDigit +"s";
                System.out.printf(blank,"");
            }

            //second for loop prints all decending numbers, beginning with the line number and ending with 1
            for (int decrement = currentLine; decrement >= 2; decrement--) {
                String value = "%" + columWidth +"s";
                System.out.printf(value,decrement);
            }

            //third for loop prints ascending numbers begenning at 2 and ending with the line number
            for (int increment = 0; increment <= currentLine; increment++) {
                if(increment != 0){
                    String value = "%" + columWidth +"s";
                    System.out.printf(value,increment);
                }
            }

            //prints a new line for each pyramid line
            System.out.println("");

        }
    }
}
