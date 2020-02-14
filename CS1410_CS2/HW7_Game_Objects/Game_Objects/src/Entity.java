public class Entity {
    private Position position = new Position();

    Entity(){

    }
    Entity(int posX,int posY){
        this.getPosition().x = posX;
        this.getPosition().y = posY;
    }

    Entity(Object object){

    }

    public Position getPosition() {return this.position; };

    public Treasure getTreasure(){ return Treasure.Wood; };

    public String getColor() { return "Fuschia "; }

    public void setPosition(int posX,int posY){
        this.position.x = posX;
        this.position.y = posY;
    }

}