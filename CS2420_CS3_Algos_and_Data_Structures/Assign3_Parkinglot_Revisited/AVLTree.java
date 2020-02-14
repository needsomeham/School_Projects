// AvlTree class
//
// CONSTRUCTION: with no initializer
//
// ******************PUBLIC OPERATIONS*********************
// void insert( node )                         --> Insert node
// void remove( removedItem , treeRoot )       --> Remove removedItem (unimplemented)
// boolean contains( findThis )                --> Return true if findThis is present
// boolean remove( node )                      --> Return true if node was present
// Comparable findMin( )                       --> Return smallest item
// Comparable findMax( )                       --> Return largest item
// boolean isEmpty( )                          --> Return true if empty; else false
// void makeEmpty( )                           --> Remove all items
// void printTree( )                           --> Print tree in sorted order
// ******************ERRORS********************************
// Throws UnderflowException as appropriate

/**
 * Implements an AVL tree.
 * Note that all "matching" is based on the compareTo method.
 * @author Mark Allen Weiss
 */
public class AVLTree<AnyType extends Comparable<? super AnyType>>
{
    /**
     * Construct the tree.
     */
    public AVLTree( )
    {
        root = null;
    }

    /**
     * Insert into the tree; duplicates are ignored.
     * @param node the item to insert.
     */
    public void insert( AnyType node )
    {
        root = insert( node, root );
    }

    /**
     * Remove from the tree. Nothing is done if x is not found.
     * @param node the item to remove.
     */
    public void remove( AnyType node )
    {
        root = remove( node, root );
    }


    /**
     * Internal method to remove from a subtree.
     * @param removedItem the item to remove.
     * @param treeRoot the node that roots the subtree.
     * @return the new root of the subtree.
     */
    private AvlNode<AnyType> remove( AnyType removedItem, AvlNode<AnyType> treeRoot)
    {
        if( treeRoot== null )
            return treeRoot;   // Item not found; do nothing

        int compareResult = removedItem.compareTo( treeRoot.element );

        if( compareResult < 0 )
            treeRoot.left = remove( removedItem, treeRoot.left );
        else if( compareResult > 0 )
            treeRoot.right = remove( removedItem, treeRoot.right );
        else if( treeRoot.left != null && treeRoot.right != null ) // Two children
        {
            treeRoot.element = findMin( treeRoot.right ).element;
            treeRoot.right = remove( treeRoot.element, treeRoot.right );
        }
        else
            treeRoot = ( treeRoot.left != null ) ? treeRoot.left : treeRoot.right;
        return balance( treeRoot );
    }

    /**
     * Method for finding the min of a tree (moving all the way to the left)
     */
    private AvlNode<AnyType> findMinRecurs(AvlNode node){
        if (node==null) {return null;}
        if (node.left == null) {
            return node;
        } else  {
            return findMinRecurs(node.left);
        }
    }

    /**
     * Find the smallest item in the tree.
     * @return smallest item or null if empty.
     */
    public AnyType findMin( )
    {
        if (root ==null) {return null;}
        return findMinRecurs(root).element;


        //not sure what this code does, but I wrote my own find min function
//        if( isEmpty( ) )
//            throw new RuntimeException( );
//        return findMin( root ).element;
    }


    /**
     * Helper method to delete min node and balance tree on way back up
     * @param node root of the tree from which to delete min
     * @param minNode node which you want to delete (should be min)
     * @return root node
     */
    private AvlNode balancedMin(AvlNode node, AvlNode minNode ){
        if ( node==null ) { return null; }
        if ( node.left == minNode ) {
            node.left = minNode.right;
            return balance(node); }
        else {
            balancedMin(node.left,minNode);
            return balance(node);
        }
    }

    /**
     * deletes the min of a tree and recursively balances the tree back on the way to the root
     */
    public  void  deleteMin( ){
        AvlNode<AnyType> minNode = findMin(root);
        root =  balancedMin(root,minNode);
     }

    /**
     * removes the min of the tree
     * @param minNode
     * @return root
     */
    private AvlNode<AnyType> deleteMin( AvlNode<AnyType> minNode )
    {
        AnyType realMin = findMin();
        balancedMin(root,(AvlNode)realMin);
        return root;
    }

    /**
     * Find the largest item in the tree.
     * @return the largest item of null if empty.
     */
    public AnyType findMax( )
    {
        if( isEmpty( ) )
            throw new RuntimeException( );
        return findMax( root ).element;
    }

    /**
     * Find an item in the tree.
     * @param findThis the item to search for.
     * @return true if x is found.
     */
    public boolean contains( AnyType findThis )
    {
        return contains( findThis, root );
    }

    /**
     * Make the tree logically empty.
     */
    public void makeEmpty( )
    {
        root = null;
    }

    /**
     * Test if the tree is logically empty.
     * @return true if empty, false otherwise.
     */
    public boolean isEmpty( )
    {
        return root == null;
    }

    /**
     * Print the tree contents in sorted order.
     */
    public void printTree( String label)
    {
        System.out.println(label);
        if( isEmpty( ) )
            System.out.println( "Empty tree" );
        else
            printTree( root,"" );
    }
    //named constant to determine the balance of a tree

    private static final int ALLOWED_IMBALANCE = 1;

    /**
     * Method for balancing a AVL tree
     * Assume t is either balanced or within one of being balanced
     * @param workingNode
     * @return balanced node
     */
    private AvlNode<AnyType> balance( AvlNode<AnyType> workingNode )
    {
        if( workingNode == null )
            return workingNode;

        if( height( workingNode.left ) - height( workingNode.right ) > ALLOWED_IMBALANCE )
            if( height( workingNode.left.left ) >= height( workingNode.left.right ) )
                workingNode = rightRotation( workingNode );
            else
                workingNode = doubleRightRotation( workingNode );
        else
        if( height( workingNode.right ) - height( workingNode.left ) > ALLOWED_IMBALANCE )
            if( height( workingNode.right.right ) >= height( workingNode.right.left ) )
                workingNode = leftRotation( workingNode );
            else
                workingNode = doubleLeftRotation( workingNode );

        workingNode.height = Math.max( height( workingNode.left ), height( workingNode.right ) ) + 1;
        return workingNode;
    }

    /**
     * Kick-oof method to determine if a node if balanced
     */
    public void checkBalance( )
    {
        checkBalance( root );
    }

    /**
     * Method to determine if a node is balanced or not
     * @param workingNode node to check balance of
     * @return height. -1 if null, else the current height of the largest subchild
     */
    private int checkBalance( AvlNode<AnyType> workingNode )
    {
        if( workingNode == null )
            return -1;

        if( workingNode != null )
        {
            int hl = checkBalance( workingNode.left );
            int hr = checkBalance( workingNode.right );
            if( Math.abs( height( workingNode.left ) - height( workingNode.right ) ) > 1 ||
                    height( workingNode.left ) != hl || height( workingNode.right ) != hr )
                System.out.println( "\n\n***********************OOPS!!" );
        }

        return height( workingNode );
    }


    /**
     * Internal method to insert into a subtree.  Duplicates are allowed
     * @param insertThis the item to insert.
     * @param treeRoot the node that roots the subtree.
     * @return the new root of the subtree.
     */
    private AvlNode<AnyType> insert( AnyType insertThis, AvlNode<AnyType> treeRoot )
    {
        if( treeRoot == null )
            return new AvlNode<>( insertThis, null, null );

        int compareResult = insertThis.compareTo( treeRoot.element );

        if( compareResult < 0 )
            treeRoot.left = insert( insertThis, treeRoot.left );
        else
            treeRoot.right = insert( insertThis, treeRoot.right );

        return balance( treeRoot );
    }

    /**
     * Internal method to find the smallest item in a subtree.
     * @param treeRoot the node that roots the tree.
     * @return node containing the smallest item.
     */
    private AvlNode<AnyType> findMin( AvlNode<AnyType> treeRoot )
    {
        if( treeRoot == null )
            return treeRoot;

        while( treeRoot.left != null )
            treeRoot = treeRoot.left;
        return treeRoot;
    }

    /**
     * Internal method to find the largest item in a subtree.
     * @param treeRoot the node that roots the tree.
     * @return node containing the largest item.
     */
    private AvlNode<AnyType> findMax( AvlNode<AnyType> treeRoot )
    {
        if( treeRoot == null )
            return treeRoot;

        while( treeRoot.right != null )
            treeRoot = treeRoot.right;
        return treeRoot;
    }

    /**
     * Internal method to find an item in a subtree.
     * @param findThis is item to search for.
     * @param treeRoot the node that roots the tree.
     * @return true if findThis is found in subtree.
     */
    private boolean contains( AnyType findThis, AvlNode<AnyType> treeRoot )
    {
        while( treeRoot != null )
        {
            int compareResult = findThis.compareTo( treeRoot.element );

            if( compareResult < 0 )
                treeRoot = treeRoot.left;
            else if( compareResult > 0 )
                treeRoot = treeRoot.right;
            else
                return true;    // Match
        }

        return false;   // No match
    }

    /**
     * Internal method to print a subtree in sorted order.
     * @param treeRoot the node that roots the tree.
     */
    private void printTree( AvlNode<AnyType> treeRoot, String indent )
    {
        if( treeRoot != null )
        {
            printTree( treeRoot.right, indent+"   " );
            System.out.println( indent+ treeRoot.element + "("+ treeRoot.height  +")" );
            printTree( treeRoot.left, indent+"   " );
        }
    }

    /**
     * Method checks the height of the tree
     * Return the height of node t, or -1, if null.
     * @param treeRoot
     */
    private int height( AvlNode<AnyType> treeRoot )
    {   if (treeRoot==null) return -1;
        return treeRoot.height;
    }


    /**
     * Rotate binary tree node with left child.
     * For AVL trees, this is a single rotation for case 1.
     * Update heights, then return new root.
     * @param node around which to rotate
     * @return new "root" (in scope of node) post rotation
     */
    private AvlNode<AnyType> rightRotation(AvlNode<AnyType> node )
    {
        AvlNode<AnyType> theLeft = node.left;
        node.left = theLeft.right;
        theLeft.right = node;
        node.height = Math.max( height( node.left ), height( node.right ) ) + 1;
        theLeft.height = Math.max( height( theLeft.left ), node.height ) + 1;
        return theLeft;
    }

    /**
     * Rotate binary tree node with right child.
     * For AVL trees, this is a single rotation for case 4.
     * Update heights, then return new root.
     * @param node around which to rotate
     * @return new "root" (in scope of node) post rotation
     */
    private AvlNode<AnyType> leftRotation(AvlNode<AnyType> node )
    {
        AvlNode<AnyType> theRight = node.right;
        node.right = theRight.left;
        theRight.left = node;
        node.height = Math.max( height( node.left ), height( node.right ) ) + 1;
        theRight.height = Math.max( height( theRight.right ), node.height ) + 1;
        return theRight;
    }

    /**
     * Double rotate binary tree node: first left child
     * with its right child; then node k3 with new left child.
     * For AVL trees, this is a double rotation for case 2.
     * Update heights, then return new root.
     * @param node around which to rotate.
     * @return new "root" (in scope of note) post rotation
     */
    private AvlNode<AnyType> doubleRightRotation( AvlNode<AnyType> node )
    {
        node.left = leftRotation( node.left );
        return rightRotation( node );

    }

    /**
     * Double rotate binary tree node: first right child
     * with its left child; then node k1 with new right child.
     * For AVL trees, this is a double rotation for case 3.
     * Update heights, then return new root.
     * @param node around which to rotate
     * @return new "root" (in scope of node) post rotation
     */
    private AvlNode<AnyType> doubleLeftRotation(AvlNode<AnyType> node )
    {
        node.right = rightRotation( node.right );
        return leftRotation( node );
    }


    private static class AvlNode<AnyType>
    {

        // Constructors
        AvlNode( AnyType theElement )
        {
            this( theElement, null, null );
        }
        AvlNode( AnyType theElement, AvlNode<AnyType> leftTree, AvlNode<AnyType> rightTree )
        {
            element  = theElement;
            left     = leftTree;
            right    = rightTree;
            height   = 0;
        }

        AnyType           element;      // The data in the node

        AvlNode<AnyType>  left;         // Left child
        AvlNode<AnyType>  right;        // Right child
        int               height;       // Height

        public AnyType getElement(){
            return this.element;
        }
    }

    /** The tree root. */
    private AvlNode<AnyType> root;


    // Test program
    public static void main( String [ ] args ) {
        AVLTree<Integer> t = new AVLTree<>();
        AVLTree<Dwarf> t2 = new AVLTree<>();

        String[] nameList = {"Snowflake", "Sneezy", "Doc", "Grumpy", "Bashful", "Dopey", "Happy", "Doc", "Grumpy", "Bashful", "Doc", "Grumpy", "Bashful"};
        for (int i=0; i < nameList.length; i++)
            t2.insert(new Dwarf(nameList[i]));

        t2.printTree( "The Tree" );

        t2.remove(new Dwarf("Bashful"));

        t2.printTree( "The Tree after delete Bashful" );
        for (int i=0; i < 8; i++) {
            t2.deleteMin();
            t2.printTree( "\n\n The Tree after deleteMin" );
        }
    }

}
