public class Crate extends Entity {
    private Treasure garbage;

    Crate(){
    }

    Crate(Treasure garbage,int posX,int posY){
        super(posX, posY);
        this.garbage = garbage;
    }

    @Override
    public Treasure getTreasure(){
        return this.garbage;
    }

    public String toString(){
        return "Crate with " + this.garbage + " at " + super.getPosition();
    }

}
