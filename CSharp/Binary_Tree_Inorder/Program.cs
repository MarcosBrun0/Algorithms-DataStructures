using System.ComponentModel.Design.Serialization;

public class TreeNode
{
    public int val;
    public TreeNode? left;
    public TreeNode? right;

    public TreeNode(int val=0, TreeNode? left =null, TreeNode? right=null)
    {
        this.val=val;
        this.left=left;
        this.right=right;
        
    }

}


public class Program
{
    public IList<int> InorderTraversal(TreeNode root)
    {

        IList<int> list = new List<int>();
        Seek(root, list);
        return list;
    }

    private IList<int> Seek(TreeNode root, IList<int> result)
    {
        if (root != null)
        {
            Seek(root.left, result);
            result.Add(root.val);
            Seek(root.right, result);
        }
        return null;

    }


    public static void Main(string[] args)
    {

    }
}