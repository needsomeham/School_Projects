public class Dragon extends Entity{
    private String color;
    Dragon(){}

    Dragon(String color,int posX, int posY){
        super(posX,posY);
        this.color = color;
    }

    @Override
    public String getColor(){
        return this.color;
    }

    public String toString() {
        return "The " + this.color + " dragon breathing fire at " + super.getPosition();
    }
    
}

