public class GregorianDate extends Date {

    GregorianDate(){
        //constructor defaults to the current date by invoking the parent class
        super();
        super.year = 1970;   //because the parent class has a default date setting the year to 1, change it to 1970 for UNIX epoch
        //finds the current (today) date from UNIX epoch
        long time = System.currentTimeMillis()+java.util.TimeZone.getDefault().getRawOffset();
        int today = (int) (time/(1000*60*60*24));
        addDays(today);

    }

    GregorianDate(int year, int month, int day) {
        //invoking the parent class's overloaded constructor
        super(year, month, day);

    }

    /*
    Method determines if it is a leap year or not.

    @AUTHOR Jacob Needham
     */
    @Override
    boolean isLeapYear(int year){
        return ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0)) ;
    }

}
