import java.util.Scanner;

public class quadratic {
    public static void main(String[] args) {
        /*
        The class quadratic takes three coefficients from the user and returns the
        real roots. If the roots are imaginary then it will tell the user that the
        roots do not exist.
         */
        //creating a scanner instance and pulling a, b, c from the user
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the three coefficients for the quadratic equation");
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();

        //calculating the roots of the quadratic
        double determinate = (b * b - 4 * a * c);
        double root1 = -b + (Math.sqrt(determinate) / 2.0);
        double root2 = -b - (Math.sqrt(determinate) / 2.0);

        //checking if the determinate has real roots and reporting the root(s)
        if ( determinate >= 0 && root1 != root2) {
            System.out.println("The roots of the equation are: " + root1 + " , " + root2);
        }
        else if (root1==root2) {
            System.out.println("The one root is " + root1);
        }
        else {
            System.out.println("There are no real roots");
        }
    }

}