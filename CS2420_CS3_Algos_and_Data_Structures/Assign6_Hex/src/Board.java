import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;


public class Board {
    public static void main(String[] args) {
        //everything works well, the only problem is that at some point it asks for a find 0. Because the whole board
        //is initizalized at 0 from the outset its tough to track the problem down.

        HexBoard redSpaces = new HexBoard(false);
        HexBoard blueSpaces = new HexBoard(true);


        // reading in the list of moves
        ArrayList masterMoves = new ArrayList();
        try {
            Scanner reader = new Scanner(new File("moves.txt"));
            while ((reader.hasNext())) {
                int value = reader.nextInt();
                masterMoves.add(value);
            }
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }

        // adding moves back to each red and blue board
        // red = odd (first move)
        // blue = even (second move)
        for (int i=0; i<masterMoves.size();i++){
            if ((i+2)%2 == 1) {
                redSpaces.add( (int) masterMoves.get(i));
            }
            else {
                blueSpaces.add( (int) masterMoves.get(i));
            }
        }

        //testing if one of the boards is a winner
        if(redSpaces.isWinner()){
            System.out.println("Red won this round");
        }
        if(blueSpaces.isWinner()){
            System.out.println("Blue won this round");
        }









        //test code to see if the space is working
        //worked before I made the game for two players
//        HexBoard gameSapace = new HexBoard(true);
//
//
//        for (int i=1; i<5; i++){
//            gameSapace.union(i,i+1);
//
//        }
//        for (int i=1; i<8; i++){
//            System.out.println("root node: " + gameSapace.find(i));;
//
//        }
//
//
    }
}
