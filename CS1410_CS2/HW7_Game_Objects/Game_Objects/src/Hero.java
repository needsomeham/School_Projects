import java.util.ArrayList;

public class Hero extends Entity {
    private String name;
    private ArrayList<Treasure> victoryList = new ArrayList<>();
    private static int heroCount;

    Hero(){
        //heroCount++;
    }

    Hero(String name,int posX,int posY) {
        super(posX,posY);
        this.name = name;
        heroCount++;
    }


    public String getName(){
        return this.name;
    }

    public int numHeros(){
        return heroCount;
    }

    public void attack(Entity thing) {
        if (thing instanceof Crate) {
            victoryList.add(thing.getTreasure());
            if (thing.getTreasure().equals(Treasure.Food) )
            System.out.printf("%s crushed the crate into bits and found %s\n", this.name, thing.getTreasure());
        }
        if (thing instanceof Dragon) {
            if (thing.getColor() == "Golden") {
                victoryList.add(Treasure.Coins);
                System.out.printf("%s bravely defeated the Golden dragon and came away with gold coins as a prize.\n", this.name);
            }
            else {
                System.out.printf("%s bravely defeated the %s dragon\n", this.name, thing.getColor());
            }
        }
    }
    public ArrayList<Treasure> getTreasures() {
        return this.victoryList;
    }

    public String toString(){
        return this.name + " is standing at " + this.getPosition();
    }
}
