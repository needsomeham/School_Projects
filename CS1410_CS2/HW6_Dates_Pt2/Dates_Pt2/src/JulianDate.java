public class JulianDate extends Date {

    JulianDate(){
        //invoking the parent's class default constructor
        super();

        //finds the current (today) date from UNIX epoch
        long time = System.currentTimeMillis()+java.util.TimeZone.getDefault().getRawOffset();
        int today = (int) (time/(1000*60*60*24) + 719164) ;
        addDays(today);
    }

    JulianDate(int year, int month, int day) {
        //invokes the parent's overloaded constructor
        super(year, month, day);

    }

    /*
    Method determines if it is a leap year or not.

    AUTHOR @Jacob Needham
    */
    boolean isLeapYear(int year){
        return (year % 4 == 0);
    }

}
