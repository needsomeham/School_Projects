
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Reviews {

    public Reviews() {

        H = new QuadraticProbingHashTable<String,WordInfo>();
    }



    public String toString() {
        int LIMIT = 20;
        return name + "\n" + H.toString(LIMIT);
    }


    private String name;
    private QuadraticProbingHashTable<String,WordInfo> H;

    public void readReviews(String filename)
            throws FileNotFoundException, IOException {
            BufferedReader in = new BufferedReader(new FileReader(filename));
            String name = null;
            String line;
            String[] words = null;

            int score = -1;
            int line_count = 0;
            while ((line = in.readLine()) != null) {
                line_count++;
                words = line.split("\\s+");
                try {
                    score = Integer.parseInt(words[0]);
                } catch (NumberFormatException e) {
                    throw new NumberFormatException("Expected integer at line " + line_count + " in file " + filename);
                }
                ReviewInfo r = new ReviewInfo(score, words);
                System.out.println(r.toString());
                if (line_count == 4) {
                    System.out.println("yep");
                }

                for (int i =1; i<words.length;i++){
                    String word = words[i].toLowerCase();
                    if (H.contains(word)) {
                        H.find(word).update(score);
                    }
                    else{
                        WordInfo tempWord = new WordInfo(word);
                        tempWord.update(score);
                        H.insert(word,tempWord);
                    }
                }
            }
            System.out.println("Number of Reviews " +  line_count);

        }
        private static class ReviewInfo {
            int score;
            String[] words;

            // Constructors
            ReviewInfo(int score, String[] words) {
                this.score = score;
                this.words = words;
            }

            public String toString() {
                StringBuilder sb = new StringBuilder();
                sb.append("Review " + score+ " Length of Review " + (words.length -1) + " ");
                for (int i = 1; i < 11 & i < words.length; i++)
                    sb.append(words[i] + " ");
                return sb.toString();
            }
        }

    public static class WordInfo {
        int totalScore;
        int numberOfOccurences;
        String word;

        // Constructors
        WordInfo(String word) {
            this.word = word;
            totalScore=0;
            numberOfOccurences = 0;
        }

        public void update(int score){
            this.totalScore+=score;
            this.numberOfOccurences++;
        }

        public String getWord(){
            return this.word;
        }

        public int getTotalScore(){
            return this.totalScore;
        }

        public double getAverageScore(){
            return (double) totalScore/ (double) numberOfOccurences;
        }

        public int getNumberOfOccurences(){
            return this.numberOfOccurences;
        }

        public String toString() {
           return "Word " + word + " [" + totalScore +", " + numberOfOccurences+"]";
        }
    }

        public static void main (String[ ]args ){

            try {
                Reviews r1 = new Reviews();
                r1.readReviews("movieReviews.txt");
                System.out.println(r1);

                //Assignment code

                //Reading in user info and converting to a useable split string
                Scanner reader = new Scanner(System.in);
                System.out.println("Type a review here:\n");
                String rawUserReview = reader.nextLine();
                rawUserReview.toLowerCase();
                String[] splitUserReview = rawUserReview.split("\\s+");

                //Assigning weighted value to user input
                double unweightedSum = 0;
                for (int i=0; i<splitUserReview.length; i++) {
                    //System.out.println("in for loop");
                    if (r1.H.find(splitUserReview[i]) != null) {
                        WordInfo tempWord = r1.H.find(splitUserReview[i]);
                        unweightedSum += tempWord.getAverageScore();
                        //System.out.println("In if statement");
                    }

                }
                double finalScore = unweightedSum/splitUserReview.length;
                System.out.println("number of words in review:" + splitUserReview.length);
                System.out.println("The review score is:" + finalScore);

                if (finalScore <= 1.75) System.out.println("Negative");
                else if (finalScore <= 2.25) System.out.println("Neutral");
                else System.out.println("Positive");


            } catch (IOException e) {
                e.printStackTrace();
            }

            WordInfo w = new WordInfo("fat");
            w.update(4);
            System.out.println(w.toString());



            //to dos:
            //prompt user to input a review
            //make score each word in the review
            // ignore words repeated more than 10% of time of in base case
            // average the total score



        }

    }
