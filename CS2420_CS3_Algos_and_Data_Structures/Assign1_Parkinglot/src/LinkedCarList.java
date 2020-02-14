public class LinkedCarList {
    private Node head;
    private Node tail;
    private int size = 0;

    //constructor
    public LinkedCarList() {
        this.size = 0;
        this.head = null;
        this.tail = null;
    }

    //useful for troubleshooting code
    public Node getHead(){
        return this.head;
    }

    //add function
    public void add(Node node) {

        if (tail == null) {
            head = tail = node;
        } else {
            tail.addNext(node);
            this.tail = node;
        }
        size++;
    }

    //returns the length of the list
    public int size() {
        return this.size;
    }

    //basically a ghetto function that linearly scans the linked list to find the node you want
    public Node get(Integer passedInt) {
        Node workingNode = head;
        for (int i = 0; i < passedInt; i++) {
            workingNode = workingNode.getNext();
        }
        return workingNode;
    }
}