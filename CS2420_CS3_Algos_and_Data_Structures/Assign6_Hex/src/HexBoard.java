import java.util.Arrays;

public class HexBoard {

    private int board[];
    private int boardWidth;
    private boolean playerOne;
    private int TOP;
    private int BOTTOM;
    private int LEFT;
    private int RIGHT;

    //general constructor if you dont know the size of the array
    public HexBoard(boolean playerOne){
        this.playerOne = playerOne;
        board = new int[126];       //really size 121 but begin indexing at 1
        Arrays.fill(board,0);
        boardWidth = (int) java.lang.Math.sqrt(board.length);

        //making final constants to store winning paths
        TOP = board.length -4;
        BOTTOM = board.length -3;
        LEFT = board.length -2;
        RIGHT = board.length -1;

    }

    //overloaded constructor if you know the size of the board
    public HexBoard(int boardSize,boolean playerOne) {
        this.playerOne = playerOne;
        board = new int[boardSize+5];
        Arrays.fill(board,0);
        boardWidth = (int) java.lang.Math.sqrt(board.length);

        //making final constants to store winning paths
        TOP = board.length -4;
        BOTTOM = board.length -3;
        LEFT = board.length -2;
        RIGHT = board.length -1;

    }

    public void printBoard(){
        for (int i=0; i<board.length; i++){
            if (i%11 ==0){
                System.out.println("\n");
            }
            System.out.println(i+": " + board[i]);
        }
    }

    public boolean isWinner(){
        if(find(TOP)==find(BOTTOM) || find(LEFT)==find(RIGHT)){
            return true;
        }
        else return false;
    }

    public boolean add(int addThis){
        if (board[addThis] == 0){
            board[addThis] = -1;
            getNeighbors(addThis);
            return true;
        }
        else {
            System.out.println("I tried to add a number that is already on the board");
            return false;
        }
    }

    private int[] getNeighbors(int checkThis){

        int NW = checkThis - boardWidth;
        int NE = checkThis - (boardWidth -1);
        int W = checkThis - 1;
        int E = checkThis + 1;
        int SW = checkThis + (boardWidth-1);
        int SE = checkThis + boardWidth;


        //checking corner cases
        //top left case
        if (checkThis == 1) {
            NW = NE = SW = W = -1;
        }
        //top right case
        if (checkThis == boardWidth) {
            NW = NE = E = SE = -1;
        }
        //bottom left case
        if (checkThis == board.length-boardWidth) {
            SE = SW = W = NW = -1;
        }
        //bottom right case
        if (checkThis == board.length) {
            SW = SE = E = NE = -1;
        }


        //checking boarder cases
        //top boarder
        if(NW<0 && NE<0) {
            NW = NE = -1;
        }
        //bottom border
        if(SW>board.length && SE>board.length) {
            SW = SE = -1;
        }
        //left boarder
        if(W%boardWidth == 0 && SW%boardWidth==0) {
            W = SW = -1;
        }
        //right boarder
        if(E%boardWidth ==1 && NE%boardWidth==1) {
            E = NE = -1;
        }




        //unioning all the neighbors for left
        //top left
        if(NW==-1 && NE==-1 && W==-1 && SW==-1) {
            union(checkThis,LEFT);
            union(checkThis,TOP);
            union(checkThis,E);
            union(checkThis,SE);
        }

        //bottom right
        if(SW==-1 && SE==-1 && W==-1) {
            union(checkThis,LEFT);
            union(checkThis,RIGHT);
            union(checkThis,NE);
            union(checkThis,NW);
            union(checkThis,E);
        }

        //main left
        if(SW==-1 && W==-1){
            union(checkThis,LEFT);
            union(checkThis,NE);
            union(checkThis,NW);
            union(checkThis,E);
            union(checkThis,SE);
        }



        //unioning all the neighbors for right
        //top right
        if(NW==-1 && NE ==-1 && E==-1) {
            union(checkThis,RIGHT);
            union(checkThis,LEFT);
            union(checkThis,W);
            union(checkThis,SW);
            union(checkThis,SE);
        }
        //bottom right
        if(NE==-1 && E==-1 && SW==-1 && SE==-1){
            union(checkThis,RIGHT);
            union(checkThis,BOTTOM);
            union(checkThis,W);
            union(checkThis,NW);
        }
        //main right
        if(NE==-1 && E==-1){
            union(checkThis,RIGHT);
            union(checkThis,NW);
            union(checkThis,W);
            union(checkThis,SW);
            union(checkThis,SE);
        }


        //unioning main top
        if(NW==-1 && NE==-1){
            union(checkThis,TOP);
            union(checkThis,W);
            union(checkThis,E);
            union(checkThis,SW);
            union(checkThis,SE);
        }


        //unioning main bottom
        if(SW==-1 && SE==-1){
            union(checkThis,BOTTOM);
            union(checkThis,W);
            union(checkThis,E);
            union(checkThis,NW);
            union(checkThis,NE);
        }
        int[] neighbors = new int[]{NW,NE,W,E,SW,SE};
        return neighbors;

    }


    //returns the root node
    public Integer find(Integer findThis){
        if ( findThis==0){
            return findThis;
        }
        if (board[findThis] < 0) {
            return findThis;
        }
        else if (board[findThis] > 0 ) {
            return find(board[findThis]);
        }
        else {
            return 0;
        }
    }

    //returns the size of the root node
    private Integer findSize(Integer findThis){
        return java.lang.Math.abs(board[find(findThis)]);
    }

    public void union(int setOne, int setTwo) {

        if(setOne ==0 || setTwo==0) {
            return;
        }

        //points the smaller node to the larger nodes root
        int size1 = findSize(setOne);
        int size2 = findSize(setTwo);
        int root1 = find(setOne);
        int root2 = find(setTwo);

        if (size1 >= size2){
            board[root2] = root1;
            board[root1] = -(size1+size2);
            //compression
            pathCompression(setTwo, root1);
        }
        else {
            board[root1] = root2;
            board[root2] = -(size1+size2);
            pathCompression(setOne,root2);
        }
    }

    private boolean pathCompression(int node,int root){
        if ( board[node] < 0){
            return true;
        }
        else {
            int temp = board[node];
            board[node] = root;
            return pathCompression(temp, root);
        }
    }


}



