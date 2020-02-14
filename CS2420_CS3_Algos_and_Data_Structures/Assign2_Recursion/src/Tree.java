// ******************ERRORS********************************
// Throws UnderflowException as appropriate

//needed for printer class that I stole from StackOverflow
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
//

import org.w3c.dom.Node;

import java.math.BigInteger;
import java.util.Random;
import java.util.ArrayList;
import java.util.Arrays;

class UnderflowException extends RuntimeException {
    /**
     * Construct this exception object.
     * @param message the error message.
     */
    public UnderflowException(String message) {
        super(message);
    }
}

public class Tree {
    final String ENDLINE = "\n";
    private BinaryNode<Integer> root;  // Root of tree
    private BinaryNode<Integer> curr;  // Last node accessed in tree
    private String treeName;     // Name of tree

    /**
     * Create an empty tree
     *
     * @param label Name of tree
     */
    public Tree(String label) {
        treeName = label;
        root = null;
    }

    /**
     * Create non ordered tree from list in preorder
     * @param arr    List of elements
     * @param label  Name of tree
     * @param height Maximum height of tree
     */
    public Tree(ArrayList<Integer> arr, String label, int height) {
        this.treeName = label;
        root = buildTree(arr, height, null);
    }

    /**
     * Create BST
     * @param arr   List of elements to be added
     * @param label Name of tree
     */
    public Tree(ArrayList<Integer> arr, String label) {
        root = null;
        treeName = label;
        for (int i = 0; i < arr.size(); i++) {
            bstInsert(arr.get(i));
        }
    }


    /**
     * Create BST from Array
     * @param arr   List of elements to be added
     * @param label Name of  tree
     */
    public Tree(Integer[] arr, String label) {
        root = null;
        treeName = label;
        for (int i = 0; i < arr.length; i++) {
            bstInsert(arr[i]);
        }
    }

    /**
     * Change name of tree
     * @param name new name of tree
     */
    public void changeName(String name) {
        this.treeName = name;
    }


    //HELPER function to aid in string printing recursion

    public String toStringHelp(BinaryNode node, String spacer){
        if (node==null){
            return "";
        }
        else {
            spacer += "  ";
            return toStringHelp(node.right, spacer) + "\n" + spacer + node.element +
                    "[" + node.parent.element + "]" + toStringHelp(node.left,spacer);
        }
    }

    /**
     * Return a string displaying the tree contents as a tree with one node per line
     * Order of complexity: O(n) (Andy said not to include helper functions)
     */
    public String toString() {
        if (root == null)
            return (treeName + " Empty tree\n");
        else {
            String spacer = "";
            return treeName + "\n" + toStringHelp(root.right,spacer) + "\n" + root.element +
                    "[" + "no parent" + "]" + toStringHelp(root.left,spacer) + "\n";
        }
    }

    /**
     * Return a string displaying the tree contents as a single line
     */
    public String toString2() {
        if (root == null)
            return treeName + " Empty tree";
        else
            return treeName + " " + toString2(root);
    }


    //HELPER class to aid in flipping a BST
    private BinaryNode<Integer> bstInsertReversed(Integer x, BinaryNode<Integer> t, BinaryNode<Integer> parent) {
        if (t == null)
            return new BinaryNode<>(x, null, null, parent);

        int compareResult = x.compareTo(t.element);

        if (compareResult > 0) {
            t.left = bstInsert(x, t.left, t);
        } else {
            t.right = bstInsert(x, t.right, t);
        }

        return t;
    }

    /**
     * reverse left and right children recursively
     * Order of complexity: O(n) (Andy said not to include helper functions)
     */
    public void flip(BinaryNode<Integer> node) {
         //flip(root);
        //What do I want this method to do? Strip children from parent, hold them in a temp array, assign each of its children to the left and right children.
        if(node.left == null) { return; }

        flip(node.left);

        Integer leftTemp = node.left.element;
        node.left.element = node.right.element;
        node.right.element = leftTemp;

        flip(node.right);

    }

/*
    //HELPER method to traverse a BST
    private Integer[] TreeTraversalInOrder(BinaryNode<Integer> node; Integer[] ) {
        TreeTraversalInOrder(node.left);
        return node.element;
        TreeTraversalInOrder(node.right);

    }
*/
    /**
     * Find successor of "curr" node in tree
     * @return String representation of the successor
     */
    public String successor() {
        if (curr == null) curr = root;
        //curr = successor(curr);
        if (curr == null) return "null";
        else return curr.toString();
    }

    /**
     * Counts number of nodes in specifed level
     * @param level Level in tree, root is zero
     * @return count of number of nodes at specified level
     */





    //----------------Works--------------------------------------------------

    //Order of complexity: O(n) (Andy said not to include helper functions)
    public int nodesInLevel(BinaryNode node, int level) {
        //recurse all children on node, check if node height == level, if null! return +1

        if (node == null) {
            return 0;
        }

        if(level == 0) {
            if (node.element != null) { return +1; }
            else { return 0; }
        }
        else if (level > -1) {
            return nodesInLevel(node.right, level-1) + nodesInLevel(node.left, level-1);
        }
        return 0;
    }

    //----------------------------------------------------------------------

    //HELPER method for printing all paths
    public void printAllPathsHelp(BinaryNode node, String masterString){
        if (node == null) {
            System.out.println(masterString);
        }
        else if (node.right != null && node.left != null) {
            masterString += " " + node.element.toString();
            printAllPathsHelp(node.right,masterString);
            printAllPathsHelp(node.left,masterString);
        }
        else if (node.left==null){
            masterString += " " + node.element.toString();
            printAllPathsHelp(node.right,masterString);
        }
        else {
            masterString += " " + node.element.toString();
            printAllPathsHelp(node.left,masterString);
        }
    }

    /**
     * Print all paths from root to leaves
     * Order of complexity: O(n)
     */
    public void printAllPaths() {
        if (root == null){
            System.out.println("No root, empty tree");
        }
        else{
            String masterString = "";
            printAllPathsHelp(root, masterString);
        }
    }

    /**
     * Print contents of levels in zig zag order starting at maxLevel
     * @param maxLevel
     */
    public void byLevelZigZag(int maxLevel) {

    }



    // ------------- should work -------------------------------------------
    //HELPER function to find max or min of a tree
    public int maxOfTree(BinaryNode node, boolean isMax) {
        if (node == null) {return (int) node.parent.element;}
        int valueLeft = maxOfTree(node.left, isMax);
        int valueRight = maxOfTree(node.right, isMax);
        if (isMax) {
            if(valueLeft> valueRight){
                return valueLeft;
            }
            else { return valueRight; }
        }
        else {
            if(valueLeft< valueRight){
                return valueLeft;
            }
            else { return valueRight; }
        }
    }

    /**
     * Counts all non-null binary search trees embedded in tree
     * @return Count of embedded binary search trees
     * Order of complexity: O(log(n)) (Andy said not to include helper functions)
     */
    public int countBST(BinaryNode node) {
        //recurse to evey node in tree: if{ root<right.value, root>right.value, left.value <= right.value} return +1
        if (node == null) {return 0;}
        if (node.left==null && node.right==null) {
            return +1;
        }
        else if (node.left == null){
            return countBST(node.right)+1;
        }
        else if (node.right == null){
            return  countBST(node.left) +1;
        }
        else if ( node.right != null && node.left != null &&
                (Integer)node.element < (Integer)node.right.element &&
                (Integer) node.element > (Integer) node.left.element){
            return 1 + countBST(node.left) + countBST(node.right);
        }
        else { return 0; }
    }


    //-------------------------------------------------------------------




    /**
     * Insert into a bst tree; duplicates are allowed
     * @param x the item to insert.
     */
    public void bstInsert(Integer x) {

        root = bstInsert(x, root, null);
    }


    /**
     * Determines if item is in tree
     * @param item the item to search for.
     * @return true if found.
     */
    public boolean contains(Integer item) {

        return bstContains(item, root);
    }



    /**
     * Remove all paths from tree that sum to less than given value
     * @param sum: minimum path sum allowed in final tree
     */
    public void pruneK(Integer sum) {
        //recurse to each node: {if sum lef child.
    }



    /**
     * Build tree given inOrder and preOrder traversals.  Each value is unique
     * @param inOrder  List of tree nodes in inorder
     * @param preOrder List of tree nodes in preorder
     */
    public void buildTreeTraversals(Integer[] inOrder, Integer[] preOrder) {
        root = null;
    }


    //----------------should work----------------------------------------------

    //HELPER function to find a node of a given value
    public BinaryNode containsValue(BinaryNode node,Integer value) {
        if (node.element == value){
            return node;
        }
        else if (node == null) {
            return null;
        }
        else if (node.left != null) {
            return containsValue(node.left, value);
        }
        else if (node.right != null) {
             return containsValue(node.right, value);
        }
        return null;
    }


    /**
     * Find the least common ancestor of two nodes
     * @param a first node
     * @param b second node
     * @return String representation of ancestor
     * Order of complexity: O(n^2) (Andy said not to include helper functions)
     */
    public String lca(BinaryNode node, Integer a, Integer b) {
        BinaryNode<Integer> ancestor = null;
        BinaryNode nodeA = containsValue(node,a);
        BinaryNode nodeB = containsValue(node,b);

        if (containsValue(node,a)==null || containsValue(node,b)==null) {
            //System.out.println(containsValue(node,a).element);
            //System.out.println(containsValue(node,b).element);
            return "\nSorry, but the tree doesnt contain " + a.toString() + " or " + b.toString();
        }


        ArrayList<BinaryNode> parentListA = new ArrayList<>();
        while (nodeA.parent != null){
            System.out.println(node.parent.element);
            BinaryNode newNode = node.parent;
            parentListA.add(newNode);
        }
        //System.out.println(parentListA);

        ArrayList<BinaryNode> parentListB = new ArrayList<>();
        while (nodeB.parent != null) {
            BinaryNode newNode = node.parent;
            parentListB.add(newNode);
        }

        for (int i =0; i < parentListA.size(); i++){
            //System.out.println("in first for loop");
            for(int j=0; j < parentListB.size(); i++){
                //System.out.println("in second for loop");
                if (parentListA.get(i) == parentListB.get(j)){
                    ancestor = parentListA.get(i);
                }
            }
        }

        if (ancestor == null) return "none";
        else return ancestor.toString();
    }

    //----------------------------------------------------




    //HELPER method to strip all values from a tree and return them as an array list
    public String stripTree(BinaryNode node,String listOfNodes) {
        if (node == null) { return ""; }
        else {
            return stripTree(node.left, listOfNodes) + " " + node.element.toString() + " " +  stripTree(node.right,listOfNodes);
        }
    }

    //HELPER function to insert mids
    public void insertMid(BinaryNode node ){

    }

    /**
     * Balance the tree
     * Order of complexity: O(n) (Andy said not to include helper functions)
     */
    public void balanceTree() {
        //root = balanceTree(root);
        String starterList = "";
        String listOfNodes = stripTree(root, starterList);
        System.out.println("the list of nodes in order" + listOfNodes);

        String[] splitStringNum = listOfNodes.split("  ");
        ArrayList<Integer> listofIntegers = new ArrayList<Integer>(splitStringNum.length);
        for (int i = 0;i<splitStringNum.length;i++){
            splitStringNum[i] = splitStringNum[i].replace(" ","");
            listofIntegers.add( Integer.parseInt(splitStringNum[i]));
        }



    }

    /**
     * In a BST, keep only nodes between range
     * @param a lowest value
     * @param b highest value
     */
    public void keepRange(Integer a, Integer b) {
     }

    //PRIVATE

     /**
     * Build a NON BST tree by preorder
     *
     * @param arr    nodes to be added
     * @param height maximum height of tree
     * @param parent parent of subtree to be created
     * @return new tree
     */
    private BinaryNode<Integer> buildTree(ArrayList<Integer> arr, int height, BinaryNode<Integer> parent) {
        if (arr.isEmpty()) return null;
        BinaryNode<Integer> curr = new BinaryNode<>(arr.remove(0), null, null, parent);
        if (height > 0) {
            curr.left = buildTree(arr, height - 1, curr);
            curr.right = buildTree(arr, height - 1, curr);
        }
        return curr;
    }

    /**
     * Internal method to insert into a subtree.
     * In tree is balanced, this routine runs in O(log n)
     *
     * @param x the item to insert.
     * @param t the node that roots the subtree.
     * @return the new root of the subtree.
     */
    private BinaryNode<Integer> bstInsert(Integer x, BinaryNode<Integer> t, BinaryNode<Integer> parent) {
        if (t == null)
            return new BinaryNode<>(x, null, null, parent);

        int compareResult = x.compareTo(t.element);

        if (compareResult < 0) {
            t.left = bstInsert(x, t.left, t);
        } else {
            t.right = bstInsert(x, t.right, t);
        }

        return t;
    }


    /**
     * Internal method to find an item in a subtree.
     * This routine runs in O(log n) as there is only one recursive call that is executed and the work
     * associated with a single call is independent of the size of the tree: a=1, b=2, k=0
     *
     * @param x is item to search for.
     * @param t the node that roots the subtree.
     *          SIDE EFFECT: Sets local variable curr to be the node that is found
     * @return node containing the matched item.
     */
    private boolean bstContains(Integer x, BinaryNode<Integer> t) {
        curr = null;
        if (t == null)
            return false;

        int compareResult = x.compareTo(t.element);

        if (compareResult < 0)
            return bstContains(x, t.left);
        else if (compareResult > 0)
            return bstContains(x, t.right);
        else {
            curr = t;
            return true;    // Match
        }
    }



    /**
     * Internal method to return a string of items in the tree in order
     * This routine runs in O(??)
     * @param t the node that roots the subtree.
     */
    private String toString2(BinaryNode<Integer> t) {
        if (t == null) return "";
        StringBuilder sb = new StringBuilder();
        sb.append(toString2(t.left));
        sb.append(t.element.toString() + " ");
        sb.append(toString2(t.right));
        return sb.toString();
    }

    // Basic node stored in unbalanced binary  trees
    private static class BinaryNode<Integer> {
        Integer element;            // The data in the node
        BinaryNode<Integer> left;   // Left child
        BinaryNode<Integer> right;  // Right child
        BinaryNode<Integer> parent; //  Parent node

        // Constructors
        BinaryNode(Integer theElement) {
            this(theElement, null, null, null);
        }

        BinaryNode(Integer theElement, BinaryNode<Integer> lt, BinaryNode<Integer> rt, BinaryNode<Integer> pt) {
            element = theElement;
            left = lt;
            right = rt;
            parent = pt;
        }


        //-------------------should work ---------------------------------------
        //HELPER function to find depth of a given node
        public int nodeDepth(BinaryNode node, Integer findThis){
            if(node.element == findThis){ return 0; }
            if( (int) findThis > (int) node.element ) {
                int depth = nodeDepth(node.right, findThis) +1;
                return depth;
            }
            else{
                int depth = nodeDepth(node.left, findThis) +1;
                return depth;
            }
        }




        public String toString(BinaryNode node) {
            StringBuilder sb = new StringBuilder();
            sb.append("Node:");
            toString(node.left);
            sb.append(element);
            if (parent == null) {
                sb.append("<>");
            } else {
                sb.append("<");
                sb.append(parent.element);
                sb.append("> \n");
            }
            return sb.toString();
        }
    }

    //-------------------------------------------------TEST-------------------------------------------------------------

    // Test program
    public static void main(String[] args) {
        long seed = 436543;
        Random generator = new Random(seed);  // Don't use a seed if you want the numbers to be different each time
        final String ENDLINE = "\n";

        int val = 60;
        final int SIZE = 8;

        Integer[] v1 = {25, 10, 60, 55, 58, 56, 14, 63, 8, 50, 6, 9};
        ArrayList<Integer> v2 = new ArrayList<Integer>();
        for (int i = 0; i < SIZE * 2; i++) {
            int t = generator.nextInt(200);
            v2.add(t);
        }
        v2.add(val);
        Integer[] v3 = {200, 15, 3, 65, 83, 70, 90};
        ArrayList<Integer> v4 = new ArrayList<Integer>(Arrays.asList(v3));
        Integer[] v = {21, 8, 5, 6, 7, 19, 10, 40, 43, 52, 12, 60};
        ArrayList<Integer> v5 = new ArrayList<Integer>(Arrays.asList(v));
        Integer[] inorder = {4, 2, 1, 7, 5, 8, 3, 6};
        Integer[] preorder = {1, 2, 4, 3, 5, 7, 8, 6};


        Tree tree1 = new Tree(v1, "Tree1:");
        Tree tree2 = new Tree(v2, "Tree2:");
        Tree tree3 = new Tree(v3, "Tree3:");
        Tree treeA = new Tree(v4, "TreeA:", 2);
        Tree treeB = new Tree(v5, "TreeB", 3);
        Tree treeC = new Tree("TreeC");


        //starting the testing of trees ------------------------------------------------

//        //testing the toString Method  -----------------------WORKS---------------------
//        System.out.println("Printing toString calls:");
//        System.out.println(tree1.toString());
//        System.out.println(tree1.toString2());
//       System.out.println(treeA.toString());

//        //testing the .flip method --------------------------WORKS--------------------------
//        treeA.flip(treeA.root);
//        System.out.println("Now flipped" + treeA.toString());
//
//
//        //Testing the .successor method
//        System.out.println(tree2.toString(tree2.root));
//        tree2.contains(val);  //Sets the current node inside the tree6 class.
//        int succCount = 5;  // how many successors do you want to see?
//        System.out.println("In Tree2, starting at " + val + ENDLINE);
//        for (int i = 0; i < succCount; i++) {
//            System.out.println("The next successor is " + tree2.successor());
//        }
//
//
//        //testing the .nodesInLevel method -----------------WORKS-----------
//        System.out.println(tree1.toString());
//        for (int mylevel = 0; mylevel < SIZE; mylevel += 2) {
//            System.out.println("Number nodes at level " + mylevel + " is " + tree1.nodesInLevel(tree1.root, mylevel));
//        }
//
//        //testing the .printAllPaths method -----------------------WORKS-----------------
//        System.out.println("All paths from tree1");
//        tree1.printAllPaths();

//        //testing the .byLevelZigZag
//        System.out.print("Tree1 byLevelZigZag: ");
//        tree1.byLevelZigZag(5);
//        System.out.print("Tree2 byLevelZigZag (3): ");
//        tree2.byLevelZigZag(3);
//        treeA.flip(treeA.root);
//

//        //testing the .countBST method
//        System.out.println(treeA.toString());
//        System.out.println("treeA Contains BST: " + treeA.countBST(treeA.root));
//        System.out.println(treeB.toString());
//        System.out.println("treeB Contains BST: " + treeB.countBST(treeB.root));
//

//        //testing the .pruneK method
//        treeB.pruneK(60);
//        treeB.changeName("treeB after pruning 60");
//        System.out.println(treeB.toString());
//        treeA.pruneK(220);
//        treeA.changeName("treeA after pruning 220");
//        System.out.println(treeA.toString());
//

//        //testing the buildTreeTraversals(order)
//        treeC.buildTreeTraversals(inorder, preorder);
//        treeC.changeName("Tree C built from inorder and preorder traversals");
//        System.out.println(treeC.toString());
//

//        //testing lca method
//        System.out.println(tree1.toString());
//        System.out.println("tree1 Least Common Ancestor of (56,61) " + tree1.lca(tree1.root,56, 61) + ENDLINE);
//        System.out.println("tree1 Least Common Ancestor of (6,25) " + tree1.lca(tree1.root,6, 25) + ENDLINE);
//        System.out.println(tree3.toString());


        //testing .balanceTree method
        tree3.balanceTree();
        tree3.changeName("tree3 after balancing");
        System.out.println(tree3.toString());


//        //testing .keepRange method
//        System.out.println(tree1.toString());
//        tree1.keepRange(10, 50);
//        tree1.changeName("tree1 after keeping only nodes between 10 and 50");
//        System.out.println(tree1.toString());
//        tree3.keepRange(3, 85);
//        tree3.changeName("tree3 after keeping only nodes between 3  and 85");
//        System.out.println(tree3.toString());


    }

}
