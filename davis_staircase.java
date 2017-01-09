/* Davis has s staircases in his house and he likes to climb 1, 2 or 3 steps at a time.
Given the respective height of each staircase s as n, find and print the number of ways he can climb each staircase
on a new line.
*/
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution 
{
    //this map acts as a cache
    private static Map<Integer, Integer> ca = new HashMap<>();
    //main function
    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();        
        for(int i = 0; i < s; i++)
        {
            int n = in.nextInt();
            System.out.println(climb(n));
        }        
    }
    
    private static int climb(int n) 
    {
        //no stairs - 0 way
        if(n < 0)
            return 0;
        //no or 1 stair - 1 way
        if(n == 0)
            return 1;
        //find no. of ways if not already in cache
        if(!ca.containsKey(n)) 
        {
            int count = climb(n-1) + climb(n-2) + climb(n-3);      
            ca.put(n, count);
        }    
        return ca.get(n);
    }
}
