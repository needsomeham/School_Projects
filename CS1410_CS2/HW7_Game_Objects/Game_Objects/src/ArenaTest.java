import org.junit.Assert;

public class ArenaTest {
    @org.junit.Test
    public void ArenaTestConstructor() {
        int sizeX = 20;
        int sizeY = 10;
        Arena uut = new Arena(sizeX, sizeY);
        String msg = "Arena::Constructor: Incorrect ";

        Assert.assertEquals(msg + "grid row size", sizeX, uut.getGrid().size());

        for (int row = 0; row < uut.getGrid().size(); row++) {
            Assert.assertEquals(msg + "grid column size at row " + Integer.toString(row), sizeY, uut.getGrid().get(row).length);
        }
    }

    @org.junit.Test
    public void ArenaTestAdd() {
        int sizeX = 20;
        int sizeY = 10;
        Arena uut = new Arena(sizeX, sizeY);
        String msg = "Arena::Add: Failed to correctly ";

        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                System.out.println("trying the swapped x,y thing");
                Assert.assertTrue(msg + "add entity at " + Integer.toString(x) + ", " + Integer.toString(y), uut.add(new Entity(x, y)));
                Assert.assertTrue(msg + "add entity into grid at " + Integer.toString(x) + ", " + Integer.toString(y), uut.getGrid().get(x)[y] != null);
            }
        }

        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                Assert.assertFalse(msg + "prevent multiple additions of entities at " + Integer.toString(x) + ", " + Integer.toString(y), uut.add(new Entity(x, y)));
            }
        }
    }

    @org.junit.Test
    public void ArenaTestMoveHero() {
        int sizeX = 20;
        int sizeY = 10;
        int treasureCount = 0;
        Arena uut = new Arena(sizeX, sizeY);
        String msg = "Arena::MoveHero: Failed to correctly ";
        Entity [] entityArray = {new Hero("Kal", 1, 1),
                new Crate(Treasure.Wood, 1, 2), new Crate(Treasure.Statue, 1, 3),
                new Crate(Treasure.Coins, 2, 1), new Crate(Treasure.Food, 2, 2), new Crate(Treasure.Rags, 2, 3),
                new Dragon("Golden", 0, 0)};

        for (Entity ent : entityArray) {
            uut.add(ent);
        }

        for (int i = 1; i < entityArray.length; i++) {
            uut.moveHero(entityArray[i].getPosition().x, entityArray[i].getPosition().y);
            treasureCount++;

            Assert.assertEquals(msg + "move hero to x position " + Integer.toString(entityArray[i].getPosition().x), uut.getHero().getPosition().x, entityArray[i].getPosition().x);
            Assert.assertEquals(msg + "move hero to y position " + Integer.toString(entityArray[i].getPosition().y), uut.getHero().getPosition().y, entityArray[i].getPosition().y);
            Assert.assertEquals(msg + "update hero treasure count to " + Integer.toString(treasureCount), treasureCount, uut.getHero().getTreasures().size());
        }

    }

    @org.junit.Test
    public void ArenaTestGetHero() {
        int sizeX = 20;
        int sizeY = 10;
        Arena uut = new Arena(sizeX, sizeY);
        String msg = "Arena::GetHero: Failed to correctly ";
        Entity [] entityArray = {new Hero("Kal", 1, 1), new Hero("Moash", 2, 2), new Hero("Rock", 3, 3)};

        Assert.assertTrue(msg + "initialize hero member to null", uut.getHero() == null);

        for (Entity ent : entityArray) {
            uut.add(ent);
            Assert.assertEquals(msg + "disallow multiple addition of Hero", entityArray[0], uut.getHero());
        }
    }

    @org.junit.Test
    public void ArenaTestGetEntityCount() {
        int sizeX = 20;
        int sizeY = 10;
        Arena uut = new Arena(sizeX, sizeY);
        String msg = "Arena::GetEntityCount: Failed to correctly ";

        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {

                if ((x + y) % 4 == 0) {
                    uut.add(new Crate(Treasure.Coins, x, y));
                }
                else if ((x + y) % 4 == 1) {
                    uut.add(new Crate(Treasure.Food, x, y));
                }
                else if ((x + y) % 4 == 2) {
                    uut.add(new Entity(x, y));
                }
                else if ((x + y) % 4 == 3) {
                    uut.add(new Dragon("Yellow", x, y));
                }
            }
        }

        Assert.assertEquals(msg + "calculate entity count" , sizeX * sizeY, uut.getEntityCount());
    }

    @org.junit.Test
    public void ArenaTestGetDragonCount() {
        int sizeX = 20;
        int sizeY = 10;
        int dragonCount = 0;
        Arena uut = new Arena(sizeX, sizeY);
        String msg = "Arena::GetDragonCount: Failed to correctly ";

        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {

                if ((x + y) % 4 == 0) {
                    uut.add(new Crate(Treasure.Coins, x, y));
                }
                else if ((x + y) % 4 == 1) {
                    uut.add(new Crate(Treasure.Food, x, y));
                }
                else if ((x + y) % 4 == 2) {
                    uut.add(new Entity(x, y));
                }
                else if ((x + y) % 4 == 3) {
                    uut.add(new Dragon("Yellow", x, y));
                    dragonCount++;
                }
            }
        }

        Assert.assertEquals(msg + "calculate dragon count" , dragonCount, uut.getDragonCount());
    }

    @org.junit.Test
    public void ArenaTestGetTreasureCount() {
        int sizeX = 20;
        int sizeY = 10;
        int [] counts = new int[5];
        Arena uut = new Arena(sizeX, sizeY);
        String msg = "Arena::GetTreasureCount: Failed to correctly ";

        for (int x = 0; x < sizeX; x++) {
            for (int y = 0; y < sizeY; y++) {
                int val = (x + y) % 7;

                if (val <= 4) {
                    uut.add(new Crate(Treasure.values()[val], x, y));
                    counts[val]++;
                }
                else if (val == 5) {
                    uut.add(new Dragon("Green", x, y));
                }
                else if (val == 6) {
                    uut.add(new Entity(x, y));
                }
            }
        }

        for (int i = 0; i < counts.length; i++) {
            Assert.assertEquals(msg + "calculate treasure count for " + Treasure.values()[i].name(), counts[i], uut.getTreasureCount(Treasure.values()[i]));
        }
    }
}