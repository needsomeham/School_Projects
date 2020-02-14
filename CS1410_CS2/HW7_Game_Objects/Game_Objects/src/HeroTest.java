import org.junit.Assert;

public class HeroTest {
    @org.junit.Test
    public void HeroTestConstructor() {
        int posX = 17;
        int posY = 18;
        String name = "Kal";
        String msg = "Hero::Constructor: Failed to update ";
        Hero uut = new Hero(name, posX, posY);

        Assert.assertEquals(msg + "Position X", posX, uut.getPosition().x);
        Assert.assertEquals(msg + "Position Y", posY, uut.getPosition().y);
        Assert.assertEquals(msg + "Name", name, uut.getName());
    }

    @org.junit.Test
    public void HeroTestGetName() {
        int posX = 17;
        int posY = 18;
        String [] nameArray = {"Kaladin", "Rock", "Teft", "Skar", "Moash", "Sigzil"};
        String msg = "Hero::GetName: Failed to update ";

        for (String name : nameArray) {
            Hero uut = new Hero(name, posX, posY);

            Assert.assertEquals(msg + "Name", name, uut.getName());
        }
    }

    @org.junit.Test
    public void HeroTestAttackAndGetTreasures() {
        int posX = 17;
        int posY = 18;
        String name = "Kal";
        String msg = "Hero::Attack: Failed to handle attacking ";
        Hero uut = new Hero(name, posX, posY);
        int treasureCount = 0;
        Entity [] entityArrayWithTreasure = {new Dragon("Golden", 1, 1), new Crate(Treasure.Food, 2, 2), new Crate(Treasure.Rags, 3, 3)};
        Entity [] entityArrayWithOutTreasure = {new Dragon("Green", 4, 4), new Entity(5, 5)};

        for (Entity i : entityArrayWithTreasure) {
            treasureCount++;
            uut.attack(i);
            Assert.assertEquals(msg + i.getClass().getName() + ", no treasure was received", treasureCount, uut.getTreasures().size());
            Assert.assertEquals(Treasure.values()[1 + treasureCount], uut.getTreasures().get(treasureCount - 1));
        }

        for (Entity i : entityArrayWithOutTreasure) {
            uut.attack(i);
            Assert.assertEquals(msg + i.getClass().getName() + ", treasure should NOT have been received", treasureCount, uut.getTreasures().size());
        }
    }

    @org.junit.Test
    public void HeroTestToString() {
        int posX = 17;
        int posY = 18;
        String [] nameArray = {"Kaladin", "Rock", "Teft", "Skar", "Moash", "Sigzil"};
        String msg = "Hero::ToString: String must contain ";

        for (String name : nameArray) {
            Hero uut = new Hero(name, posX, posY);

            Assert.assertTrue(msg + "'" + name + "'", uut.toString().contains(name));
            Assert.assertTrue(msg + "'" + Integer.toString(posX) + "'", uut.toString().contains(Integer.toString(posX)));
            Assert.assertTrue(msg + "'" + Integer.toString(posY) + "'", uut.toString().contains(Integer.toString(posY)));

            posX += 2;
            posY += 3;
        }
    }
}