import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class SpellChecker {
    public static void main(String[] args) throws FileNotFoundException {

        // Step 1: Demonstrate tree capabilities
        testTree();

        // Step 2: Read the dictionary and report the tree statistics
        BinarySearchTree<String> dictionary = readDictionary();
        reportTreeStats(dictionary);

        // Step 3: Perform spell checking
        Scanner letter = new Scanner(new File("Letter.txt"));
        System.out.println();
        System.out.println("-- Incorrect Words --");
        System.out.println();
        //more formatting

        while (letter.hasNext()) {
            //replacing all non letter characters with nothing
            String word = letter.next().replaceAll("[,:.!?()]","").toLowerCase();

            //testing to see if the word is in the dictionary
            if(!dictionary.search(word)) {
                System.out.println(word);
            }
        }
    }

    /**
     * This method is used to help develop the BST, also for the grader to
     * evaluate if the BST is performing correctly.
     */
    public static void testTree() {
        BinarySearchTree<String> tree = new BinarySearchTree<>();

        //
        // Add a bunch of values to the tree
        tree.insert("Olga");
        tree.insert("Tomeka");
        tree.insert("Benjamin");
        tree.insert("Ulysses");
        tree.insert("Tanesha");
        tree.insert("Judie");
        tree.insert("Tisa");
        tree.insert("Santiago");
        tree.insert("Chia");
        tree.insert("Arden");

        //
        // Make sure it displays in sorted order
        tree.display("--- Initial Tree State ---");
        reportTreeStats(tree);

        //
        // Try to add a duplicate
        if (tree.insert("Tomeka")) {
            System.out.println("oops, shouldn't have returned true from the insert");
        }
        tree.display("--- After Adding Duplicate ---");
        reportTreeStats(tree);

        //
        // Remove some existing values from the tree
        tree.remove("Olga");    // Root node
        tree.remove("Arden");   // a leaf node
        tree.display("--- Removing Existing Values ---");
        reportTreeStats(tree);

        //
        // Remove a value that was never in the tree, hope it doesn't crash!
        tree.remove("Karl");
        tree.display("--- Removing A Non-Existent Value ---");
        reportTreeStats(tree);
    }

    /**
     * This method is used to report on some stats about the BST
     */
    public static void reportTreeStats(BinarySearchTree<String> tree) {
        System.out.println("-- Tree Stats --");
        System.out.printf("Total Nodes : %d\n", tree.numberNodes());
        System.out.printf("Leaf Nodes  : %d\n", tree.numberLeafNodes());
        System.out.printf("Tree Height : %d\n", tree.height());
    }

    /**
     * This method reads the dictionary and constructs the BST to be
     * used for the spell checking.
     */
    public static BinarySearchTree<String> readDictionary() throws FileNotFoundException  {
        //honestly I dont understand the next line of code to read in the file. I borrowed the code from Chandler Oaks
        Scanner scanner = new Scanner(new File("Dictionary.txt"));
        BinarySearchTree<String> tree = new BinarySearchTree<>();
        //list to hold the sorted lis
        ArrayList<String> sortedList = new ArrayList<>();
        //reading in the dictionary into the list
        while (scanner.hasNextLine()) {
            String word = scanner.nextLine();
            sortedList.add(word);
        }
        //not sure what scanner.close() does
        scanner.close();
        //the idea to randomize this java list came from canvas
        java.util.Collections.shuffle(sortedList, new java.util.Random(System.currentTimeMillis()));
        //building a for loop to place each newly randomized word into the list
        int length = sortedList.size();
        for(int i = 0; i < length; i++ ){
            tree.insert(sortedList.get(i));
        }

        return tree;
    }
}
