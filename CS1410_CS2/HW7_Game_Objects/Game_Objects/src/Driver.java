/**
 * Assignment 7 for CS 1410
 * @brief The program demonstrates a more complex use of object-oriented programming.
 *
 * @author James Dean Mathias
 */
public class Driver {
    public static void main(String[] args) {

        Arena gameArena = new Arena(10, 10);
        addGameEntities(gameArena);
        System.out.println("--- Arena status before moving the hero ---");
        System.out.printf("There are %d entities\n", gameArena.getEntityCount());
        System.out.printf("There are %d dragons\n", gameArena.getDragonCount());
        System.out.printf("There are %d wood treasures\n", gameArena.getTreasureCount(Treasure.Wood));
        System.out.printf("There are %d statue treasures\n", gameArena.getTreasureCount(Treasure.Statue));
        System.out.printf("There are %d food treasures\n", gameArena.getTreasureCount(Treasure.Food));
        System.out.printf("There are %d coins treasures\n", gameArena.getTreasureCount(Treasure.Coins));
        System.out.printf("There are %d rag 'treasures'\n", gameArena.getTreasureCount(Treasure.Rags));
        System.out.println();

        gameArena.moveHero(4,4);
        gameArena.moveHero(5,5);
        gameArena.moveHero(3,4);
        gameArena.moveHero(6,6);
        gameArena.moveHero(3,4);
        gameArena.moveHero(2,6);

        System.out.println();
        gameArena.reportHero();

        System.out.println("--- Arena status after moving the hero ---");
        System.out.printf("There are %d entities\n", gameArena.getEntityCount());
        System.out.printf("There are %d dragons\n", gameArena.getDragonCount());
        System.out.printf("There are %d wood treasures\n", gameArena.getTreasureCount(Treasure.Wood));
        System.out.printf("There are %d statue treasures\n", gameArena.getTreasureCount(Treasure.Statue));
        System.out.printf("There are %d food treasures\n", gameArena.getTreasureCount(Treasure.Food));
        System.out.printf("There are %d coins treasures\n", gameArena.getTreasureCount(Treasure.Coins));
        System.out.printf("There are %d rag 'treasures'\n", gameArena.getTreasureCount(Treasure.Rags));
    }

    /**
     * @brief Adds some sample entities to the arena so the hero has something to do
     *
     * @author James Dean Mathias
     */
    public static void addGameEntities(Arena arena) {
        System.out.println("--- Initializing Arena ---");
        arena.add(new Hero("Pat", 3,4));
        arena.add(new Dragon("Red", 4, 4));
        arena.add(new Dragon("Golden", 6,6));
        arena.add(new Crate(Treasure.Wood, 1, 1));
        arena.add(new Crate(Treasure.Food,5,5));
        arena.add(new Crate(Treasure.Rags,2, 6));
        arena.add(new Crate(Treasure.Statue, 3, 3));
        arena.add(new Crate(Treasure.Coins, 3, 4));
        arena.add(new Hero("Kelly", 8, 2));
        System.out.println();
    }
}
