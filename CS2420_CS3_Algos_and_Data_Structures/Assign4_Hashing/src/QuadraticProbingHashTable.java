
// QuadraticProbing Hash table class
//
// CONSTRUCTION: an approximate initial size or default of 101
//
// ******************PUBLIC OPERATIONS*********************
// bool insert( x )       --> Insert x
// bool remove( x )       --> Remove x
// bool contains( x )     --> Return true if x is present
// void makeEmpty( )      --> Remove all items


import java.util.ArrayList;

/**
 * Probing table implementation of hash tables.
 * Note that all "matching" is based on the equals method.
 * @author Mark Allen Weiss
 */
public class QuadraticProbingHashTable<K,V>
{
    /**
     * Construct the hash table.
     */
    public QuadraticProbingHashTable( )
    {
        this( DEFAULT_TABLE_SIZE );
        this.keyList = new ArrayList<>();
    }

    /**
     * Construct the hash table.
     * @param size the approximate initial size.
     */
    public QuadraticProbingHashTable( int size )
    {
        allocateArray( size );
        doClear( );
        this.keyList = new ArrayList<>();
    }

    /**
     * Insert into the hash table. If the item is
     * already present, do nothing.
     * @param k the item to insert.
     * @param v the coresponding object to insert
     */
    public boolean insert( K k,V v )
    {
        // Insert x as active
        int currentPos = findPos( k );
        if( isActive( currentPos ) ) {
            return false;
        }
        keyList.add(k);

        array[ currentPos ] = new HashEntry<V>( v, true );
        theSize++;

        // Rehash; see Section 5.5
        if( ++occupiedCt > array.length / 2 )
            rehash( );

        return true;
    }

    public String toString (int limit){
        StringBuilder sb = new StringBuilder();
        int ct=0;
        for (int i=0; i < array.length && ct < limit; i++){
            if (array[i]!=null && array[i].isActive) {
                sb.append( i + ": " + array[i].value + "\n" );
                ct++;
            }
        }
        return sb.toString();
    }

    /**
     * Expand the hash table.
     */
    private void rehash( )
    {
        HashEntry<V> [ ] oldArray = array;

        // Create a new double-sized, empty table
        allocateArray( 2 * oldArray.length );
        occupiedCt = 0;
        theSize = 0;

        //Make a copy table
        QuadraticProbingHashTable<K,V> tempTable = new QuadraticProbingHashTable<>(this.array.length);
        tempTable.array = this.array.clone();
        tempTable.keyList = this.keyList;

        this.keyList.clear();
        for (int i = 0; i < this.array.length; i++){
            if (this.array[i] != null) {
                this.array[i].isActive = false;
            }
        }

        // Copy table over
        for(int i =0; i<tempTable.keyList.size(); i++ )
            insert(keyList.get(i), tempTable.find(keyList.get(i)));
    }

    /**
     * Method that performs quadratic probing resolution.
     * @param k the item to search for.
     * @return the position where the search terminates.
     */
    private int findPos( K k )
    {
        int offset = 1;
        int currentPos = myhash( k );

        while( array[ currentPos ] != null &&
                ! ((Reviews.WordInfo) array[ currentPos ].value).getWord().equals( k ) )
        {
            currentPos += offset;  // Compute ith probe
            offset += 2;
            if( currentPos >= array.length )
                currentPos -= array.length;
        }

        return currentPos;
    }

    /**
     * Remove from the hash table.
     * @param k the item to remove.
     * @return true if item removed
     */
    public boolean remove( K k, V v )
    {
        int currentPos = findPos( k );
        if( isActive( currentPos ) )
        {
            keyList.remove(k);
            array[ currentPos ].isActive = false;
            theSize--;
            return true;
        }
        else
            return false;
    }

    /**
     * Get current size.
     * @return the size.
     */
    public int size( )
    {
        return theSize;
    }

    /**
     * Get length of internal table.
     * @return the size.
     */
    public int capacity( )
    {
        return array.length;
    }

    /**
     * Find an item in the hash table.
     * @param k the item to search for.
     * @return true if item is found
     */
    public boolean contains( K k )
    {
        int currentPos = findPos( k );
        return isActive( currentPos );
    }

    /**
     * Find an item in the hash table.
     * @param k the item to search for.
     * @return the matching object.
     */
    public V find( K k )
    {
        int currentPos = findPos( k );
        if (!isActive( currentPos )) {
            return null;
        }
        else {
            return array[currentPos].value;
        }
    }

    /**
     * Return true if currentPos exists and is active.
     * @param currentPos the result of a call to findPos.
     * @return true if currentPos is active.
     */
    private boolean isActive( int currentPos )
    {
        return array[ currentPos ] != null && array[ currentPos ].isActive;
    }

    /**
     * Make the hash table logically empty.
     */
    public void makeEmpty( )
    {
        doClear( );
    }

    private void doClear( )
    {
        occupiedCt = 0;
        for( int i = 0; i < array.length; i++ )
            array[ i ] = null;
    }

    private int myhash( K k)
    {
        int hashVal = k.hashCode( );

        hashVal %= array.length;
        if( hashVal < 0 )
            hashVal += array.length;

        return hashVal;
    }

    private static class HashEntry<V>
    {
        public V value; // the object
        public boolean isActive;  // false if marked deleted

        public HashEntry( V value )
        {
            this( value, true );
        }

        public HashEntry( V value, boolean i )
        {

            this.value = value;
            this.isActive = i;
        }
    }

    private static final int DEFAULT_TABLE_SIZE = 101;

    private HashEntry<V> [ ] array;       // The array of elements
    private int occupiedCt;               // The number of occupied cells
    private int theSize;                  // Current size
    private ArrayList<K> keyList;         // Contains all keys for the hash table

    /**
     * Internal method to allocate array.
     * @param arraySize the size of the array.
     */
    private void allocateArray( int arraySize )
    {
        array = new HashEntry[ nextPrime( arraySize ) ];
    }

    /**
     * Internal method to find a prime number at least as large as n.
     * @param n the starting number (must be positive).
     * @return a prime number larger than or equal to n.
     */
    private static int nextPrime( int n )
    {
        if( n % 2 == 0 )
            n++;

        for( ; !isPrime( n ); n += 2 )
            ;

        return n;
    }

    /**
     * Internal method to test if a number is prime.
     * Not an efficient algorithm.
     * @param n the number to test.
     * @return the result of the test.
     */
    private static boolean isPrime( int n )
    {
        if( n == 2 || n == 3 )
            return true;

        if( n == 1 || n % 2 == 0 )
            return false;

        for( int i = 3; i * i <= n; i += 2 )
            if( n % i == 0 )
                return false;

        return true;
    }


    // Simple main
    public static void main( String [ ] args )
    {
        QuadraticProbingHashTable<String,String> H = new QuadraticProbingHashTable<>( );


        long startTime = System.currentTimeMillis( );

        final int NUMS = 2000000;
        final int GAP  =   37;

        System.out.println( "Checking... (no more output means success)" );


        for( int i = GAP; i != 0; i = ( i + GAP ) % NUMS )
            H.insert( ""+i,""+i );
        for( int i = GAP; i != 0; i = ( i + GAP ) % NUMS )
            if( H.insert( ""+i,""+i ) )
                System.out.println( "OOPS!!! " + i );
        for( int i = 1; i < NUMS; i+= 2 )
            H.remove( ""+i,""+i );

//        for( int i = 2; i < NUMS; i+=2 )
//            if( !H.contains( ""+i,""+i ) )
//                System.out.println( "Find fails " + i );
//
//        for( int i = 1; i < NUMS; i+=2 )
//        {
//            if( H.contains( ""+i,""+i ) )
//                System.out.println( "OOPS!!! " +  i  );
//        }

        long endTime = System.currentTimeMillis( );

        System.out.println( "Elapsed time: " + (endTime - startTime) );
        System.out.println( "H size is: " + H.size( ) );
        System.out.println( "Array size is: " + H.capacity( ) );
    }

}

