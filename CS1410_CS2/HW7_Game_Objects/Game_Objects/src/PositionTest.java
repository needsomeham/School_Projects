import org.junit.Assert;

public class PositionTest {
    @org.junit.Test
    public void PositionTestConstructor() {
        int posX = 4;
        int posY = 5;
        Position uut = new Position(posX,  posY);

        Assert.assertEquals(posX, uut.x);
        Assert.assertEquals(posY, uut.y);
    }

    @org.junit.Test
    public void PositionTestToString() {
        int posX = 4;
        int posY = 5;
        Position uut = new Position(posX,  posY);
        String expStr = "(4, 5)";

        Assert.assertEquals(expStr, uut.toString());
    }
}
