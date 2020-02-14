import org.junit.Assert;

public class CrateTest {
    @org.junit.Test
    public void CrateTestConstructor() {
        int posX = 8;
        int posY = 80;
        String msg = "Crate::Constructor: Failed to update ";
        Treasure item = Treasure.Coins;
        Crate uut = new Crate(item, posX,  posY);

        Assert.assertEquals(msg + "treasure", item, uut.getTreasure());
        Assert.assertEquals(msg + "position x", posX, uut.getPosition().x);
        Assert.assertEquals(msg + "position y", posY, uut.getPosition().y);
    }

    @org.junit.Test
    public void CrateTestGetTreasure() {
        String msg = "Crate::GetTreasure: Failed to update ";

        for (Treasure item : Treasure.values()){
            Crate uut = new Crate(item, 9,  90);

            Assert.assertEquals(msg + "treasure", item, uut.getTreasure());
        }
    }

    @org.junit.Test
    public void CrateTestToString() {
        String msg = "Crate::ToString: String must contain ";

        for (Treasure item : Treasure.values()){
            Crate uut = new Crate(item, 10,  100);

            Assert.assertTrue(msg + "'" +item.toString() + "'", uut.toString().contains(item.toString()));
            Assert.assertTrue(msg + "'" + uut.getPosition().toString() + "'", uut.toString().contains(uut.getPosition().toString()));
        }
    }
}