import java.util.Scanner;

public class ISBN {
    public static void main(String[] args){
        /*
        The class ISBN will create an ISBN number from the number the
        user inputs. ISBN preforms a checksum to see if the digits add to 10.
        If they do then add an X to the end of the number, if not append
        the checksum to the end.
         */

        //Getting the ISBN from the user
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first 9 digits of an ISBN: ");
        int ISBNNumber = input.nextInt();
        int ISBNWork = ISBNNumber;


        //This breaks each integer off of the ISBN and stores it as an integer
        int d1 = (ISBNWork / 100000000);
        ISBNWork -= d1*100000000;
        int d2 = (ISBNWork / 10000000);
        ISBNWork -= d2*10000000;
        int d3 = (ISBNWork / 1000000);
        ISBNWork -= d3*1000000;
        int d4 = (ISBNWork / 100000);
        ISBNWork -= d4*100000;
        int d5 = (ISBNWork / 10000);
        ISBNWork -= d5*10000;
        int d6 = (ISBNWork / 1000);
        ISBNWork -= d6*1000;
        int d7 = (ISBNWork / 100);
        ISBNWork -= d7*100;
        int d8 = (ISBNWork / 10);
        ISBNWork -= d8*10;
        int d9 = (ISBNWork);


        //Creating Checksum function
        int checksum = (d1 + d2*2 + d3*3 + d4*4 + d5*5 + d6*6 + d7*7 + d8*8 + d9*9) % 11;


        //if the checksum is = 10, then the last digit is an X
        if (checksum == 10){
            System.out.print("The ISBN is: " );
            System.out.print(d1);
            System.out.print(d2);
            System.out.print(d3);
            System.out.print(d4);
            System.out.print(d5);
            System.out.print(d6);
            System.out.print(d7);
            System.out.print(d8);
            System.out.print(d9 + "X");
        }
        //else make the last digit the checksum value
        else{
            System.out.print("The ISBN is: ");
            System.out.print(d1);
            System.out.print(d2);
            System.out.print(d3);
            System.out.print(d4);
            System.out.print(d5);
            System.out.print(d6);
            System.out.print(d7);
            System.out.print(d8);
            System.out.print(d9);
            System.out.print(checksum);
        }
        }
}