import java.util.ArrayList;
public class Arena {
    private ArrayList<Entity[]> grid = new ArrayList<>();
    private Hero heroClass = new Hero();
    private int x;
    private int y;

    Arena(){}
    Arena(int sizeX,int sizeY){
        for (int i = 0; i < sizeX; i++){
            this.grid.add(new Entity[sizeY]);
        }
        this.x = sizeX;
        this.y = sizeY;
    }

    public ArrayList<Entity[]> getGrid(){ return this.grid; }

    public Hero getHero(){ return this.heroClass; }

    public int getEntityCount(){
        int entityCount = 0;
        for (int i =0; i<this.x;i++){
            for (int j = 0; j<this.y;j++){
                if (this.grid.get(i)[j] instanceof Entity) {
                  entityCount++;
                }
            }
        }
        return entityCount;
    }

    public int getDragonCount(){
        int dragonCount = 0;
        for (int i =0; i<this.x;i++){
            for (int j = 0; j<this.y;j++){
                if (this.grid.get(i)[j] instanceof Dragon) {
                    dragonCount++;
                }
            }
        }
        return dragonCount;
    }

    public int getTreasureCount(Treasure findTreasure){
        int coins = 0;
        int food = 0;
        int rags = 0;
        int wood = 0;
        int statue =0;
        for (int i =0; i<this.x;i++){
            for (int j = 0; j<this.y;j++){
                if (this.grid.get(i)[j] instanceof Crate) {
                if (this.grid.get(i)[j].getTreasure() == Treasure.Coins){ coins++; }
                if (this.grid.get(i)[j].getTreasure() == Treasure.Food){ food++; }
                if (this.grid.get(i)[j].getTreasure() == Treasure.Rags){ rags++; }
                if (this.grid.get(i)[j].getTreasure() == Treasure.Wood){ wood++; }
                if (this.grid.get(i)[j].getTreasure() == Treasure.Statue){ statue++; }
                }

            }
        }
        switch (findTreasure) {
            case Food:
                return food;
            case Rags:
                return rags;
            case Coins:
                return coins;
            case Wood:
                return wood;
            case Statue:
                return statue;
                default:
                    return 0;
        }
    }


//    public boolean add(Entity thing){
//        if (this.grid.get(thing.getPosition().x)[thing.getPosition().y]==null){
//            if (thing instanceof Hero && heroClass.numHeros()>=1){
//                this.heroClass = (Hero) thing;
//                this.grid.get(thing.getPosition().x)[thing.getPosition().y] = thing;
//                System.out.printf("Successfully added 'Pat standing at %s' to the arena.\n",this.heroClass.getPosition().toString());
//            }
//            if (thing instanceof Dragon){
//                this.grid.get(thing.getPosition().x)[thing.getPosition().y] = thing;
//                System.out.printf("Successfully added 'The %s dragon breathing fire at %s' to the arena.\n", thing.getColor(),thing.getPosition().toString());
//            }
//            if (thing instanceof Crate){
//                this.grid.get(thing.getPosition().x)[thing.getPosition().y] = thing;
//                System.out.printf("Successfully added 'Crate with %s at %s' to the game.\n",thing.getTreasure(),thing.getPosition().toString());
//            }
//            return true;
//        }
//       else {return false; }
//        else {
//            if (thing instanceof Crate){
//                System.out.printf("Could not add 'Crate with %s at %s' because another entity is already there.",thing.getTreasure(),thing.getPosition().toString());
//            }
//            if (thing instanceof Hero){
//                System.out.printf("Could not add '%s standing at %s' because there is already a hero in the arena.",((Hero) thing).getName(),thing.getPosition().toString());
//            }
//            return false; }
//    }


    public boolean add(Entity thing){
        if (this.grid.get(thing.getPosition().x)[thing.getPosition().y] == null) {
            if (!(thing instanceof Hero) || (thing instanceof Hero && (heroClass.numHeros() >= 1))) {
                this.grid.get(thing.getPosition().x)[thing.getPosition().y] = thing;
                return true;
            } else { return false; }
        }

        else return false;
    }


    public void moveHero(int xLoc, int yLoc){
        Position temp = this.heroClass.getPosition();
        if (this.grid.get(xLoc)[yLoc] != null ) {
            this.heroClass.attack(this.grid.get(xLoc)[yLoc]);
            System.out.printf("Pat moved to %s\n",heroClass.getPosition().toString());
            this.grid.get(xLoc)[yLoc] = null;
        }
        this.heroClass.setPosition(xLoc,yLoc);
        this.grid.get(temp.x)[temp.y] = null;
    }



    public void reportHero(){
        System.out.printf("--- Hero report for %s ---\n",heroClass.getName());
        System.out.printf("Position: %s\n",this.heroClass.getPosition().toString());
        System.out.println("Treasures:\n" +
                "  Food\n" +
                "  Coins\n" +
                "  Rags\n");
    }
}


