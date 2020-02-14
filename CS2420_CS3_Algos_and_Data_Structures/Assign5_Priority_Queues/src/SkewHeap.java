public class SkewHeap<E extends Comparable<?>> {
    //skew heaps finds the location that the insert needs to be put in
    //then rotates the tree at every node that was effected back up the tree to the root.

    private Term root;
    int count;


    //constructing the skew heap with no input
    public SkewHeap() {
        this.root = null;
        count=0;
    }

    //Overloaded constructor of the root
    public SkewHeap(Term e){
        this.root = e;
    }

    /**
     * Takes a node and adds it to the tree
     * @param node
     * @return true if node is added
     */
    public boolean inset(Term node) {
        if ( node == null) {
            return false;
        }
        else if ( this.root == null) {
            this.root = node;
            return true;
        }
        else {
            count++;
            this.root = merge(this.root,node);
            return true;
        }
    }

    /**
     * Switches the children of the node
     * @param node the node of which the children need to be flipped
     * @return flipped node
     */
    public Term flip(Term node){
            Term temp = node.left;
            node.left = node.right;
            node.right = temp;
            return node;
    }

    /**
     * Finds and returns the max of the heap
     * @return max node
     */
    public Term deleteMax() {
        if (this.root == null){
            return null;
        }
            Term workingMax = this.root;
            this.root = merge(this.root.right,this.root.left);
            return workingMax;
    }

    /**
     * Merges two nodes skew heap style. Node1 should be the larger of the two nodes
     * @param node1 larger of two nodes to insert
     * @param node2 smaller of two nodes to insert
     * @return merged root of two trees
     */
    public Term merge(Term node1, Term node2) {

        //base cases
        if (node1==null) {
            return node2;
        }
        if (node2 == null){
            return node1;
        }


        //alternate method to merging trees, more explicit than the next option
        Term largerNode;
        if (node1.compareTo(node2)>0) {
            node1.right = merge(node1.right,node2);
            largerNode = node1;
        }
        else{
            node2.right = merge(node2.right,node1);
            largerNode = node2;
        }
        flip (largerNode);
        return largerNode;



        //method to find larger node based on splitting tree along upper right node lines
//        if (node1.compareTo(node2) <= 0) {
//            Term tempRight = node1.right;
//            node1.right = node1.left;
//            node1.left = merge(node2,tempRight);
//            return node1;
//        }
//        else {
//            return merge(node2,node1);
//        }


    }



}
