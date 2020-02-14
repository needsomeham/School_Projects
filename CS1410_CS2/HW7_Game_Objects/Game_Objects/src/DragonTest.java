import org.junit.Assert;

public class DragonTest {
    @org.junit.Test
    public void DragonTestConstructor() {
        int posX = 11;
        int posY = 12;
        String color = "Blellow";
        String msg = "Dragon::Constructor: Failed to update ";
        Dragon uut = new Dragon(color, posX, posY);

        Assert.assertEquals(msg + "Position X", posX, uut.getPosition().x);
        Assert.assertEquals(msg + "Position Y", posY, uut.getPosition().y);
        Assert.assertEquals(msg + "Color", color, uut.getColor());
    }

    @org.junit.Test
    public void DragonTestGetColor() {
        String[] strArray = {"red", "green", "blue", "black", "purple"};
        String msg = "Dragon::GetColor: Failed to update ";

        for (String color : strArray) {
            Dragon uut = new Dragon(color, 13, 14);

            Assert.assertEquals(msg + "Color", color, uut.getColor());
        }
    }

    @org.junit.Test
    public void DragonTestToString() {
        int posX = 15;
        int posY = 16;
        String[] strArray = {"red", "green", "blue", "black", "purple"};
        String msg = "Dragon::ToString: The string result must contain ";

        for (String color : strArray) {
            Dragon uut = new Dragon(color, posX, posY);

            Assert.assertTrue(msg + "'" + color + "'", uut.toString().contains(color));
            Assert.assertTrue(msg + "'" + Integer.toString(posX) + "'", uut.toString().contains(Integer.toString(posX)));
            Assert.assertTrue(msg + "'" + Integer.toString(posY) + "'", uut.toString().contains(Integer.toString(posY)));

            posX++;
            posY += 2;
        }
    }
}