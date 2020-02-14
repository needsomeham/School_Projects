public class JulianDate {
    private int day = 1;
    private int month = 1;
    private int year = 1;

    JulianDate(){
        //finds the current (today) date from UNIX epoch
        long time = System.currentTimeMillis()+java.util.TimeZone.getDefault().getRawOffset();
        int today = (int) (time/(1000*60*60*24) + 719164) ;
        addDays(today);
    }

    JulianDate(int year, int month, int day){
        //overloaded constructor that takes day, month, and year from the user
        this.year = year;
        this.month = month;
        this.day = day;
    }

    /*
    Method returns the numer of days in a month (1-12) or returns a 0 if error.

    AUTHOR @Jacob Needham
     */
    private int getNumberOfDaysInMonth(int year, int month){
        switch (month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12: return 31;

            case 4:
            case 6:
            case 9:
            case 11: return 30;

            case 2:
                if (this.isLeapYear(year)) { return 29; }
                else { return 28; }
            default: return 0;
        }
    }

    /*
    Method returns the number of days in either a normal or leap year.

    AUTHOR @Jacob Needham
     */
    private int getNumberOfDaysInYear(int year){
        if (this.isLeapYear()) { return 366; }
        else {return 365;}
    }

    /*
    Method returns the name of the month based on the input (1-12) else returns 0 error

    AUTHOR @Jacob Needham
     */
    private String getMonthName(int Month){
        switch (month){
            case 1: return "January";
            case 2: return "February";
            case 3: return "March";
            case 4: return "April";
            case 5: return "May";
            case 6: return "June";
            case 7: return "July";
            case 8: return "August";
            case 9: return "September";
            case 10: return "October";
            case 11: return "November";
            case 12: return "December";
            default: return "ERROR";
        }
    }

    /*
    Getter method to return private variable month.

    AUTHOR @Jacob Needham
     */
    public String getCurrentMonthName(){
        return getMonthName(this.month);
    }

    /*
    Method determines if it is a leap year or not.

    AUTHOR @Jacob Needham
     */
    private boolean isLeapYear(int year){
        return (year % 4 == 0);
    }

    /*
    Getter method to return if leap year or not.

    AUTHOR @Jacob Needham
     */
    public boolean isLeapYear(){
        return this.isLeapYear(this.year);
    }

    /*
    Adds a number of days to the current date of the class.

    AUTHOR @Jacob Needham
     */
    public  void addDays(int days){
        for (int count = 0; count < days; count++) {
            this.day += 1;
            if (this.day > this.getNumberOfDaysInMonth(this.year,this.month)) {
                this.month +=1;
                this.day = 1;
            }
            if (this.month> 12){
                this.year +=1;
                this.month = 1;
            }
        }
    }

    /*
    Subtracts a number or days from the current date of the class.

    AUTHOR @Jacob Needham
     */
    public void subtractDays(int days) {
        for (int count = 0; count < days; count++) {
            this.day -= 1;
            if (this.day < 1) {
                this.month -= 1;
                if (this.month < 1) {
                    this.year -= 1;
                    this.month = 12;
                }
                this.day = this.getNumberOfDaysInMonth(this.year, this.month);
            }
        }
    }

    /*
    Method prints the numerical month name, day, and year.

    AUTHOR @Jacob Needham
     */
    public void printShortDate() {
        System.out.printf("%d/%d/%d",this.month,this.day,this.year);
    }

    /*
    Method prints the month name, day, and year.

    AUTHOR @Jacob Needham
     */
    public void printLongDate(){
        System.out.printf("%s %d, %d",this.getMonthName(this.month),this.day,this.year);
    }

    /*
    Getter method to return private variable month.

    AUTHOR @Jacob Needham
     */
    public int getCurrentMonth(){
        return this.month;
    }

    /*
    Getter method to return private variable year.

    AUTHOR @Jacob Needham
     */
    public int getCurrentYear() {
        return this.year;
    }

    /*
    Getter method to return private variable day.

    AUTHOR @Jacob Needham
     */
    public int getCurrentDayOfMonth(){
        return this.day;
    }

}