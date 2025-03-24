// Data: 19/03/2025
// Local: 101
// Authors: Costa, Marcos Burno, Almeida, Enzo

public class Solution()
{
    public int SmallestEvenMultiple(int n)
    {
        if(n % 2 == 0)
            return n;

        return n * 2;
    }

    public static void Main(String[] args)
    {
       Solution s = new Solution();
       Console.WriteLine(s.SmallestEvenMultiple(5));

    }

}
