import org.junit.Assert;

public class EntityTest {
    @org.junit.Test
    public void EntityTestConstructor() {
        int posX = 4;
        int posY = 5;
        Entity uut = new Entity(posX,  posY);

        Assert.assertEquals(posX, uut.getPosition().x);
        Assert.assertEquals(posY, uut.getPosition().y);
    }

    @org.junit.Test
    public void EntityTestGetPosition() {
        int posX = 6;
        int posY = 7;
        Entity uut = new Entity(posX,  posY);

        Assert.assertEquals(posX, uut.getPosition().x);
        Assert.assertEquals(posY, uut.getPosition().y);
    }

    @org.junit.Test
    public void setPosition() {
        int posX = 8;
        int posY = 9;
        Entity uut = new Entity(0,  0);

        uut.setPosition(posX, posY);
        Assert.assertEquals(posX, uut.getPosition().x);
        Assert.assertEquals(posY, uut.getPosition().y);
    }
}