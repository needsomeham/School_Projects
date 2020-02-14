//public class Term<AnyType implements Comparable<? super AnyType>>{
public class Term implements Comparable<Term> {

    public long freq;
    public String word;
    public Term left;
    public Term right;
    private int numTerms;

    public Term(String word, long freq){
        this.word = word;
        this.freq = freq;
    }

    public String toString(){
        return "Wt: " + freq + "\t " + word + "\n";
    }

    public int compareTo(Term t2){
        if (this.freq==t2.freq) return 0;
        else if (this.freq < t2.freq) return -1;
        return 1;
    }

    public int getNumTerms(){
        return this.numTerms;
    }

    public boolean setNumberTerms(int input){
        numTerms = input;
        return true;
    }
}

