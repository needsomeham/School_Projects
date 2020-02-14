public class Recursion {
    public static void main(String[] args) {

        int[] sumMe = { 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 };
        System.out.printf("Array Sum: %d\n", arraySum(sumMe, 0));

        int[] minMe = { 0, 1, 1, 2, 3, 5, 8, -42, 13, 21, 34, 55, 89 };
        System.out.printf("Array Min: %d\n", arrayMin(minMe, 0));

        String[] amISymmetric =  {
                "You can cage a swallow can't you but you can't swallow a cage can you",
                "I still say cS 1410 is my favorite class"
        };
        for (String test : amISymmetric) {
            String[] words = test.toLowerCase().split(" ");
            System.out.println();
            System.out.println(test);
            System.out.printf("Is word symmetric: %b\n", isWordSymmetric(words, 0, words.length - 1));
        }

        double weights[][] = {
                { 51.18 },
                { 55.90, 131.25 },
                { 69.05, 133.66, 132.82 },
                { 53.43, 139.61, 134.06, 121.63 }
        };
        System.out.println();
        System.out.println("--- Weight Pyramid ---");
        for (int row = 0; row < weights.length; row++) {
            for (int column = 0; column < weights[row].length; column++) {
                double weight = computePyramidWeights(weights, row, column);
                System.out.printf("%.2f ", weight);
            }
            System.out.println();
        }

        char image[][] = {
                {'*','*',' ',' ',' ',' ',' ',' ','*',' '},
                {' ','*',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ',' ','*','*',' ',' '},
                {' ','*',' ',' ','*','*','*',' ',' ',' '},
                {' ','*','*',' ','*',' ','*',' ','*',' '},
                {' ','*','*',' ','*','*','*','*','*','*'},
                {' ',' ',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ',' ',' ',' ',' ',' ','*',' '},
                {' ',' ',' ','*','*','*',' ',' ','*',' '},
                {' ',' ',' ',' ',' ','*',' ',' ','*',' '}
        };
        int howMany = howManyOrganisms(image);
        System.out.println();
        System.out.println("--- Labeled Organism Image ---");
        for (char[] line : image) {
            for (char item : line) {
                System.out.print(item);
            }
            System.out.println();
        }
        System.out.printf("There are %d organisms in the image.\n", howMany);

    }


    /*
    Function adds up the integers of an array starting at an index position in the array
    */
    public static long arraySum(int[] data, int position){
        if (position<0 || position >= data.length) { return 0; }
        if (position == data.length-1){
            return data[position];
        }
        long sum = 0;
        sum += arraySum(data, position+1) + data[position];
        return sum;
    }

    /*
    Function finds the minimum of an array.
    */
    public static int arrayMin(int[] data, int position){
        if (data.length-1 == position){
            return data[position];
        }
        if (data[position]<arrayMin(data,position+1)){
            return data[position];
        }
        else { return arrayMin(data,position+1); }
    }

    /*
    Function tests if a string (sentance) is symmetric or not. Base cases assume that one word or no words
    is a symmetric case.
     */
    public static boolean isWordSymmetric(String[] words, int start, int end){
        if (words.length == 0 || words.length ==1 ){ return true; }
        if (start==end) { return true; }
        if (words[start].equalsIgnoreCase(words[end])){
            return isWordSymmetric(words,start+1,end-1);
        }
        return false;
    }

    /*
    Function adds up the weight of the integers of a pyramid according to the weights above it.
     */
    public static double computePyramidWeights(double[][] weights, int row, int column){
        if (row < 0 || column < 0) { return 0; }
        if (row >= weights.length || column >= weights[row].length) { return 0; }
        double totalWeight = 0;
        totalWeight += weights[row][column] + .5*computePyramidWeights(weights,row-1,column)+.5*computePyramidWeights(weights,row-1,column-1);
        return totalWeight;
    }

    /*
    Function counts the number of organisms in an array. It then changes a grouping of organisms to a given letter.
     */
    public static int howManyOrganisms(char[][] image) {
        char a = 'a';
        int count = 0;
        for (int row =0; row<image.length; row++){
            for (int column=0; column<image[row].length; column++){
                if (image[row][column] == '*') {
                    recursive(image, row, column, a);
                    a++;
                    count++;
                }
            }
        }
        return count;
    }

    /*
    Function simply is a support function that finds the surrounding organisms if they are touching a known organism.
     */
    public static void recursive (char[][] image, int row, int col, char a){
        if (row < 0 || col < 0) { return; }
        if (row >= image.length || col >= image[row].length) { return; }
        if (image[row][col] == '*'){
            image[row][col] = a;
            recursive(image,row+1,col,a);
            recursive(image,row,col+1,a);
            recursive(image,row-1,col,a);
            recursive(image,row,col-1,a);
        }
    }

}
