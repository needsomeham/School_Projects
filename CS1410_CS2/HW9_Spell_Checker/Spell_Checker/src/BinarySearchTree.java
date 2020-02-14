public class BinarySearchTree <E extends Comparable<E>> {
    private TreeNodes root = null;
    private int numberOfNodes;
    private int theHeight;

    //inserts a value into the tree, does not allow duplicates.
    //If the value is already in the tree do not add the duplicate and return false, true otherwise.
    boolean insert(E value){
        if (root == null) {
            TreeNodes node = new TreeNodes(value);
            this.root = node;
            numberOfNodes++;
            return true;
        }
        else {
            TreeNodes parent = null;
            TreeNodes node = root;
            while (node != null) {
                parent = node;
                if (value.compareTo(node.value) < 0) { //(value < node.value
                    node = node.left;
                }
                else if (value.compareTo(node.value) >0){
                    node = node.right;
                }
                else {
                    return false;
                }
            }
            // Parent is where we came from, the node to insert on
            TreeNodes newNode = new TreeNodes(value);
            if (value.compareTo(parent.value) < 0) { //value < parent.value
                parent.left = newNode;
            }
            else {
                parent.right = newNode;
            }
            numberOfNodes++;
            return true;
        }
    }

    //deletes a value from the tree.
    //If the value was in the tree and deleted, return true, otherwise, return false.
    boolean remove(E value){
        //if ( !search(value) ) { return false; }
        TreeNodes parent = null;
        TreeNodes node = root;
        boolean done = false;
        while (!done && node != null) {
            if (node.value.compareTo(value) > 0) {  //node.value > value
                parent = node;
                node = node.left;
            }
            else if (node.value.compareTo(value) < 0) { //node.value < value
                parent = node;
                node = node.right;
            }
            else {
                done = true;
            }
        }

        if (node ==null){
            return  false;
        }

        if (node.left == null) {
            if (parent == null) {
                root = node.right;
            }
            else {
                if (parent.value.compareTo(value) < 0) { //parent.value < value
                    parent.right = node.right;
                }
                else {
                    parent.left = node.right;
                }
            }
        }
        else {
            TreeNodes parentOfRight = node;
            TreeNodes rightMost = node.left;
            while (rightMost.right != null) {
                parentOfRight = rightMost;
                rightMost = rightMost.right;
            }
            node.value = rightMost.value;
            if (parentOfRight.right == rightMost) {
                parentOfRight.right = rightMost.left;
            }
            else {
                parentOfRight.left = rightMost.left;
            }
        }
        numberOfNodes--;
        return true;
    }

    //tests to see if a value exists in the tree.
    boolean search(E value){
        TreeNodes node = root;
        while (node != null && value != node.value) { //node != null && value != node.value
            if (value.compareTo(node.value) < 0) { //value < node.value
                node = node.left;
            }
            else {
                node = node.right;
            }
        }
        if (node == null) return false;
        return true;
    }

    //Performs an in-order traversal of the tree, displaying the value at each node.
    //Use the message parameter as a header/title for the traversal.
    void display(String message){
        traverseInOrder(this.root);
        System.out.println();
    }

    private void traverseInOrder(TreeNodes node) {
        if (node == null) return;

        traverseInOrder(node.left);
        System.out.printf("%s, ", node.value);
        traverseInOrder(node.right);
    }

    //returns a count of all nodes in the tree.
    int numberNodes(){
       return (this.numberOfNodes);
    }

    //returns a count of all the leaf nodes in the tree.
    int numberLeafNodes(){
        return recursionLeaf(this.root);
    }

    private int recursionLeaf(TreeNodes node){
        if (node.value == null) { return 0; }
        if (node.right == null && node.left==null) { return 1; }
        if (node.left == null) {
            return recursionLeaf(node.right);
        }
        if (node.right == null) {
            return recursionLeaf(node.left);
        }
        return recursionLeaf(node.left) + recursionLeaf(node.right);
    }

    //returns the height of the tree.
    int height(){
        this.theHeight = heightFinder(this.root);
        return this.theHeight;
    }

    private int heightFinder(TreeNodes nodes){
        if (nodes == null) { return 0;}
        if (nodes.left == null && nodes.right == null) {return 0;}
        int leftHeight = heightFinder(nodes.left);
        int rightHeight = heightFinder(nodes.right);
        if(leftHeight > rightHeight) {
            return leftHeight +1;
        }
        else {
            return rightHeight +1;
        }
    }



    public class TreeNodes {
        public E value;
        public TreeNodes left;
        public TreeNodes right;

        public TreeNodes(E value) {
            this.value = value;
        }

    }



}
