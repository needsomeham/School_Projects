public class Position {
    int x;
    int y;
    Position(){}

    Position(int posX, int posY){
        this.x = posX;
        this.y = posY;
    }

    public String toString() {
        return "("  + this.x + ", " + this.y + ")";
    }


}
