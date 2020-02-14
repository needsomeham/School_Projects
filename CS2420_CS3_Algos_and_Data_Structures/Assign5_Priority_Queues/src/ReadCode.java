import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.io.File;


public class ReadCode {
    public static void main(String[] args) {
        //reading in the list of words and their # occurrences to a java array with Term storing each words
        ArrayList<Term> masterList = new ArrayList<>();
        try {
            Scanner reader = new Scanner(new File("SortedWords.txt"));
            while ((reader.hasNext())) {
                String word = reader.next();
                long freq = reader.nextInt();
                Term tempTerm = new Term(word, freq);
                masterList.add(tempTerm);
            }
        }
        catch (Exception ex) {
            ex.printStackTrace();
        }

        //reading input from user
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a phrase that you would like to search for:");
        String findThis = sc.next();
        System.out.println("Enter the number of words you would like as probable suggestions:");
        long counter = sc.nextLong();


        //Skew Heap to hold all "found" words. Importance is based on the # occurrences
        SkewHeap<Term> foundWordsSkew = new SkewHeap<>();


        //binary search function to find an occurrence of the word in the list then add it all to the skew heap
        boolean notFound = true;
        float currentSize = masterList.size()-1;
        int indexLocation = (int) currentSize/2;
        int iter = 0;

        while (notFound) {
            //assigns the character of the list based on the current location of the pointer
            String foundWord = masterList.get(indexLocation).word;
            char firstLetterFound = foundWord.charAt(0);

            //if the function finds the value in the array
            if (masterList.get(indexLocation).word.startsWith(findThis)) {
                while (masterList.get(indexLocation+iter).word.startsWith(findThis)) {
                    //System.out.println(indexLocation+iter);
                    foundWordsSkew.inset(masterList.get(indexLocation+iter));
                    iter++;
                }
                iter = -1;
                while (masterList.get(indexLocation+iter).word.startsWith(findThis)) {
                    //System.out.println(indexLocation+iter);
                    foundWordsSkew.inset(masterList.get(indexLocation+iter));
                    iter--;
                }
                break;
            }

            //if the search needs to go to the left ie. search < value
            if (findThis.compareTo(masterList.get(indexLocation).word)<0) {
                currentSize = currentSize/2;
                indexLocation -= currentSize/2;
                continue;
            }

            //if the search needs to go to the right ie. search > value
            else if (findThis.compareTo(masterList.get(indexLocation).word)>0){
                currentSize = currentSize/2;
                indexLocation += currentSize/2;
                continue;
            }

            //catch all non-indexed inputs
            else{
                System.out.println("The array doesnt contain the character " + findThis);
                break;
            }
        }

        //printing skew heap
        for (int i=0; i<counter; i++ ){
            System.out.println(foundWordsSkew.deleteMax());
        }

//        int printCount = 0;
//        while (foundWordsSkew.deleteMax() != null) {
//            if (foundWordsSkew.deleteMax() == null) {
//                System.out.println(printCount);
//                break;
//            }
//            System.out.println(foundWordsSkew.deleteMax());
//            printCount++;
//        }


//        System.out.println();
//        //test code to verify that the text is actually being read into the array
//        for (int i = 0; i < 7; i++) {
//            System.out.println(masterList.get(i).word + " " + masterList.get(i).freq);
//        }


        //trial code to test if skewHeap class works
//        SkewHeap<Term> trial = new SkewHeap<Term>();
//
//        String[] numbers = new String[6];
//        numbers[0] = "One";
//        numbers[1] = "Two";
//        numbers[2] = "Three";
//        numbers[3] = "Four";
//        numbers[4] = "Five";
//        numbers[5] = "Six";
//
//        for (int i = 0; i< 6; i++){
//            Term tempTerm = new Term(numbers[i],i+1);
//            trial.inset(tempTerm);
//        }
//
//        System.out.println("pop max " + trial.deleteMax());
//        System.out.println("pop max " + trial.deleteMax());
//        System.out.println("pop max " + trial.deleteMax());
//
//        System.out.println("pop max " + trial.deleteMax());
//        System.out.println("pop max " + trial.deleteMax());
//        System.out.println("pop max " + trial.deleteMax());
//       }


    }
}
