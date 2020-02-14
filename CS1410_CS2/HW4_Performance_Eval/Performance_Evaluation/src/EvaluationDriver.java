/**
 * Assignment 4 for CS 1410
 * This program evaluates the linear and binary searching, along
 * with comparing performance difference between the selection sort
 * and the built-in java.util.Arrays.sort.
 *
 * @author James Dean Mathias
 */
public class EvaluationDriver {
    static final int MAX_VALUE = 1_000_000;
    static final int MAX_ARRAY_SIZE = 100_000;
    static final int ARRAY_INCREMENT = 20_000;
    static final int NUMBER_SEARCHES = 50_000;

    public static void main(String[] args) {

        demoLinearSearchUnsorted();
        demoLinearSearchSorted();
        demoBinarySearchSelectionSort();
        demoBinarySearchFastSort();

    }


    /**
     * Creates an array of size howMany and populates it with random
     * numbers between 0 and maxValue.
     *
     * @author Jacob Needham
     */
    public static int[] generateNumbers(int howMany, int maxValue) {
        if (howMany <= 0 ) { return null; }
        int randomNumberList[] = new int[howMany];
        for (int i=0 ; i < howMany; i++){
            randomNumberList[i] = (int) (Math.random()*maxValue);
        }
        return randomNumberList;
    }

    /**
     * linear search method that searches an array of data for the
     * specified value, returns true/false
     *
     * @author Jacob Needham
     */
    public static boolean linearSearch(int[] data, int search){
        for (int i=0; i < data.length; i++) {
            if (data[i] == search) {
                return true;
            }
        }
        return false;
    }


    /**
     * Binary search method that searches an array of data for the
     * specified value and returns true/false
     *
     * @author Jacob Needham
     */
    public static boolean binarySearch(int[] data, int search){
        int lowestValue = 0;
        int highestValue = data.length -1;
        //boolean what = false;
        while (highestValue>=lowestValue){
            int midPoint = (lowestValue + highestValue)/2;
            if (search<data[midPoint]){
                highestValue = midPoint -1;
            }
            else if (search == data[midPoint]) { return true; }
            else {
                lowestValue = midPoint +1;
            }
        }
        return false;
    }


    /**
     * Sorts an array from highest to lowest
     *
     * @author Jacob Needham
     */
    public static void selectionSort(int[] data){
        for (int c=0; c < data.length-1; c++ ) {
            int currentMinIndex = c;
            for (int j = c+1; j < data.length ; j++ ) {
                if (data[j] < data[currentMinIndex]) {
                    currentMinIndex = j;
                }
            }
            int holdingBin = data[currentMinIndex];
            data[currentMinIndex]= data[c];
            data[c] = holdingBin;
            }
    }

    /**
     * Demonstrates linear searching over an unsorted array
     *
     * @author Jacob Needham
     */
    public static void demoLinearSearchUnsorted() {
        System.out.println("--- Linear Search Timing (unsorted) ---");
        for (int arraySize = ARRAY_INCREMENT; arraySize <= MAX_ARRAY_SIZE ;arraySize+=ARRAY_INCREMENT){
            int[] pleaseSort = generateNumbers(arraySize,MAX_VALUE);
            double timeBefore = System.currentTimeMillis();
            int valueCount =0;
            for (int i = 0; i < NUMBER_SEARCHES; i++){
                int findThis = (int) (Math.random()*MAX_VALUE);
                if (linearSearch(pleaseSort,findThis)){
                    valueCount++;
                }
            }
            double timeAfter = System.currentTimeMillis();
            double finalTime = timeAfter-timeBefore;
            printStuff(arraySize,valueCount,finalTime);
        }


    }
    /**
     * Demonstrates linear searching over a sorted array
     *
     * @author Jacob Needham
     */
    public static void demoLinearSearchSorted() {
        System.out.println("--- Linear Search Timing (Selection Sort) ---");
        for (int arraySize = ARRAY_INCREMENT; arraySize <= MAX_ARRAY_SIZE ;arraySize+=ARRAY_INCREMENT){
            int[] pleaseSort = generateNumbers(arraySize,MAX_VALUE);
            double timeBefore = System.currentTimeMillis();
            selectionSort(pleaseSort);
            int valueCount =0;
            for (int i = 0; i < NUMBER_SEARCHES; i++){
                int findThis  = (int) (Math.random()*MAX_VALUE);
                if (linearSearch(pleaseSort, findThis)) {
                    valueCount++;
                }
            }
            double timeAfter = System.currentTimeMillis();
            double finalTime = timeAfter-timeBefore;
            printStuff(arraySize,valueCount,finalTime);
        }

    }
    /**
     * Demonstrates binary searching when using a Selection Sort
     *
     * @author Jacob Needham
     */
    public static void demoBinarySearchSelectionSort() {
        System.out.println("--- Binary Search Timing (Selection Sort) ---");
        for (int arraySize = ARRAY_INCREMENT; arraySize <= MAX_ARRAY_SIZE ;arraySize+=ARRAY_INCREMENT){
            int[] pleaseSort = generateNumbers(arraySize,MAX_VALUE);
            double timeBefore = System.currentTimeMillis();
            selectionSort(pleaseSort);
            int valueCount =0;
            for (int i = 0; i < NUMBER_SEARCHES; i++){
                int findThis = (int) (Math.random()*MAX_VALUE);
                if (binarySearch(pleaseSort,findThis)){
                    valueCount++;
                }
            }
            double timeAfter = System.currentTimeMillis();
            double finalTime = timeAfter-timeBefore;
            printStuff(arraySize,valueCount,finalTime);
        }
    }

    /**
     * Demonstrates binary searching when using the build in Arrays.sort
     *
     * @author Jacob Needham
     */
    public static void demoBinarySearchFastSort() {
        System.out.println("--- Binary Search Timing (Arrays.sort) ---");
        for (int arraySize = ARRAY_INCREMENT; arraySize <= MAX_ARRAY_SIZE ;arraySize+=ARRAY_INCREMENT){
            int[] pleaseSort = generateNumbers(arraySize,MAX_VALUE);
            double timeBefore = System.currentTimeMillis();
            java.util.Arrays.sort(pleaseSort);
            int valueCount =0;
            for (int i = 0; i < NUMBER_SEARCHES; i++){
                int findThis = (int) (Math.random()*MAX_VALUE);
                if (java.util.Arrays.binarySearch(pleaseSort,findThis) > 0) {
                    valueCount++;
                }
            }
            double timeAfter = System.currentTimeMillis();
            double finalTime = timeAfter-timeBefore;
            printStuff(arraySize,valueCount,finalTime);
        }
    }


    /**
     * A simple print function that correctly formats the output to look like the assignment.
     *
     * @author Jacob Needham
     */
    public static void printStuff(int arraySize, int valueCount, double finalTime) {
        System.out.println("Number of items       : " + arraySize);
        System.out.println("Times value was found : " + valueCount);
        System.out.println("Total search time     : " + finalTime + " ms");
        System.out.println("");
    }
}
