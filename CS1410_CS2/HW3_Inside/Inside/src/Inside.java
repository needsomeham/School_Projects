/**
 * Assignment 3 for CS 1410
 * This program determines if points are contained within circles or rectangles.
 *
 * @author James Dean Mathias
 * @author Jacob Needham
 */
public class Inside {
    /**
     * This is the primary driver code to test the "inside" capabilities of the
     * various functions.
     *
     * @author James Dean mathias
     * @author Jacob Needham
     */
    public static void main(String[] args) {
        double[] ptX = { 1, 2, 3, 4 };
        double[] ptY = { 1, 2, 3, 4 };
        double[] circleX = { 0, 5 };
        double[] circleY = { 0, 5 };
        double[] circleRadius = { 3, 3 };
        double[] rectLeft = { -2.5, -2.5 };
        double[] rectTop = { 2.5, 5.0 };
        double[] rectWidth = { 6.0, 5.0 };
        double[] rectHeight = { 5.0, 2.5 };

        //for-loop tests all circle points
        System.out.println("--- Report of Points and Circles --- ");
        for ( int circIndex = 0; circIndex < circleX.length; circIndex++) {
            for (int locationIndex = 0; locationIndex < ptX.length; locationIndex++) {
                reportPoint(ptX[locationIndex], ptY[locationIndex]);
                if (isPointInsideCircle(ptX[locationIndex], ptY[locationIndex], circleX[circIndex], circleY[circIndex], circleRadius[circIndex])) {
                    System.out.printf(" is inside ");
                }
                else {
                    System.out.printf(" is outside ");
                }
                reportCircle(circleX[circIndex], circleY[circIndex], circleRadius[circIndex]);
            }
        }
        //for-loop tests all rectangle points
        System.out.println("\n--- Report of Points and Rectangles --- ");
        for ( int recNum = 0; recNum < circleX.length; recNum++) {
            for (int locationIndex = 0; locationIndex < ptX.length; locationIndex++) {
                reportPoint(ptX[locationIndex], ptY[locationIndex]);
                if(isPointInsideRectangle(ptX[locationIndex],ptY[locationIndex],rectLeft[recNum],rectTop[recNum],rectWidth[recNum],rectHeight[recNum])) {
                    System.out.printf(" is inside ");
                }
                else {
                    System.out.printf(" is outside ");
                }
                reportRectangle(rectLeft[recNum],rectTop[recNum],rectWidth[recNum],rectHeight[recNum]);
            }
        }
    }

    static void reportPoint(double x, double y){
        //prints the details for a single point
        String point = "Point("+x+","+y+")";
        System.out.print(point);
    }

    static void reportCircle(double x, double y, double r){
        //prints the details for the circle
        String circle ="Circle("+x+","+y+") Radius:"+r+"";
        System.out.println(circle);
    }

    static void reportRectangle(double left, double top, double width, double height) {
        //prints the details for the rectangle
        String rectangle = "Rectangle("+left+","+top+","+width+","+height+")";
        System.out.println(rectangle);
    }

    static boolean isPointInsideCircle(double ptX, double ptY, double circleX, double circleY, double circleRadius){
        //prints nothing but tests if the point is inside the circle. Returns a true or false
        return Math.sqrt(Math.pow(ptX-circleX,2) + Math.pow(ptY-circleY,2)) <= circleRadius;
    }

    static boolean isPointInsideRectangle(double ptX, double ptY, double rLeft, double rTop, double rWidth, double rHeight){
        //prints nothing but tests if the point is inside the rectangle. Returns a true or false if x falls on the range of x values its inside
        return rLeft<=ptX && ptX<=(rLeft+rWidth) && (rTop-rHeight)<=ptY && ptY<=rTop;
    }

}