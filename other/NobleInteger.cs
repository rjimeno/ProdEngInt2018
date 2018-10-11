//using System;
 
public class Solution {
     
    //public int solve(List<int> A)
    public int solve(List<int> A)
    {
        int[] arr = A.ToArray();
        Array.Sort(arr);
 
        // Return a Noble element if present
        // before last.
        int n = arr.Length;
        for (int i = 0; i < n-1; i++)
        {
            if (arr[i] == arr[i+1])
                continue;
 
            // In case of duplicates, we
            // reach last occurrence here.
            if (arr[i] == n-i-1)
                //return arr[i];
                return 1;
        }
 
        if (arr[n-1] == 0)
            //return arr[n-1];
            return 1;
 
        return -1;
    }
     
    // Driver code
    /* static public void Main ()
    {
        int [] arr = {10, 3, 20, 40, 2};
        int res = nobleInteger(arr);
        if (res != -1)
        Console.Write("The noble integer is "
                                      + res);
        else
            Console.Write("No Noble Integer "
                                  + "Found");
         
    }*/
}
