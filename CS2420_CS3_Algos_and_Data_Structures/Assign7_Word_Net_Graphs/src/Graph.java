import javax.print.DocFlavor;
import java.io.File;
import java.rmi.activation.ActivationGroup_Stub;
import java.util.*;

public class Graph {
    int numVertex;  // Number of vertices in the graph.
    GraphNode[] graphNodes;  // Adjacency list for graph.
    String graphName;  //The file from which the graph was created.


    public Graph() {
        this.numVertex = 0;
        this.graphName = "";
    }

    public Graph(int numVertex) {
        this.numVertex = numVertex;
        graphNodes = new GraphNode[numVertex];
        for (int i = 0; i < numVertex; i++) {
            graphNodes[i] = new GraphNode( i );
        }
    }

    public boolean addEdge(int source, int destination) {
        if (source < 0 || source >= numVertex) return false;
        if (destination < 0 || destination >= numVertex) return false;
        //add edge
        graphNodes[source].addEdge( source, destination );
        return true;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append( "The Graph " + graphName + " \n" );

        for (int i = 0; i < numVertex; i++) {
            sb.append( graphNodes[i].toString() );
        }
        return sb.toString();
    }

    public void makeGraph(String filename) {
        try {
            graphName = filename;
            Scanner reader = new Scanner( new File( filename ) );
            System.out.println( "\n" + filename );
            numVertex = reader.nextInt();
            graphNodes = new GraphNode[numVertex];
            for (int i = 0; i < numVertex; i++) {
                graphNodes[i] = new GraphNode( i );
            }
            while (reader.hasNextInt()) {
                int v1 = reader.nextInt();
                int v2 = reader.nextInt();
                graphNodes[v1].addEdge( v1, v2 );
            }
            reader.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


    public void clearAllPred() {
        for (int i = 0; i < numVertex; i++) {
            graphNodes[i].p1.clear();
            graphNodes[i].p2.clear();
        }
    }

    /**
     * Creates a string from two lists of parent nodes
     *
     * @param list1: list of parents for node1
     * @param list2: list of parents for node2
     * @return concatinated list of nodes in path
     */
    public String reportPath(ArrayList<Integer> list1, ArrayList<Integer> list2) {
        StringBuilder sb = new StringBuilder();
        for ( Integer element:list1){
            sb.append(element + " ");
        }
        for ( int i=list2.size()-1; i >=0; i--){
            sb.append(list2.get(i) + " ");
        }
        return sb.toString();
    }

    /**
     * LCA Helper function. Finds all parents of a node and returns them in an Array list.
     * Requires a list that contains the node to start
     *
     * @param list: ArrayList containing node to start with
     * @return list: list of nodes from current node to root
     */
    public ArrayList<Integer> parentPath(ArrayList<Integer> list){
        GraphNode workingNode = graphNodes[list.get(list.size()-1)];
        if(workingNode.succ.size() == 0) {
            return list;
        }
        list.add(workingNode.succ.get(0).to);
//        for (int i=0; i<workingNode.succ.size();i++){
//        }
        return parentPath(list);
    }


    //working on a brute force method to check all solutions and find shortest using a queue
    public ArrayList<Integer> parentPathV2(ArrayList<Integer> list){

        GraphNode workingNode = graphNodes[list.get(list.size()-1)];
        while (workingNode.succ.size() != 0) {
           // list.add()
        }


        for (int index=0; index< list.size(); index++){
            if(workingNode.succ.size() == 0) {
                return list;
            }

        }

        for (int i=0; i<workingNode.succ.size();i++){
            list.add(workingNode.succ.get(i).to);
          //  if()
        }
        return parentPathV2(list);
    }

    /**
     * LCA helper function to find the number of edges between a node and its LCA
     *
     * @param list: list of ancestral nodes. LIST MUST START AT NODE
     * @param LCA: node to check to
     * @return number of edges
     */
    public Integer howManyToLCA(ArrayList<Integer> list, int LCA){
        int count = 0;
        for(int i=0; i<list.size(); i++){
            if (list.get(i) == LCA) { return count; }
            else { count++; }
            }
        return -1;

    }

    /**
     * Computes the least common ancestor of v1 and v2, prints the length of the path, the ancestor, and the path itself.
     *
     * @param v1: first vertex
     * @param v2: second vertex
     * @return returns the length of the shortest ancestral path.
     */
    public int lca(int v1, int v2, boolean print) {

        //Finding LAC

        //Getting list of nodes from v1 to root
        GraphNode node1 = graphNodes[v1];
        ArrayList parentListPrimer1 = new ArrayList();
        parentListPrimer1.add(node1.nodeID);
        ArrayList parentList1 = parentPath(parentListPrimer1);

        //getting list of nodes form v2 to root
        GraphNode node2 = graphNodes[v2];
        ArrayList parentListPrimer2 = new ArrayList();
        parentListPrimer2.add(node2.nodeID);
        ArrayList parentList2 = parentPath(parentListPrimer2);

        //Comparing lists to find the LCA
        int lca = -1;
        for (int i=0;i<parentList1.size();i++) {
            if (parentList2.contains(parentList1.get(i))){
                lca = (int) parentList1.get(i);
                break;
            }
            else {
                //System.out.println("there is no common ancestor");
            }
        }


        //Distance

        //distance traveled from one node to other
        int distNode1 = howManyToLCA(parentList1,lca);
        int disNode2 = howManyToLCA(parentList2,lca);
        int totalDist = distNode1 + disNode2;


        //Traveled Nodes map for report Path

        ArrayList<Integer> v1Path = new ArrayList<>();
        v1Path = (ArrayList<Integer>) parentList1.clone();
        ArrayList<Integer> v2Path = new ArrayList<>();
        v2Path = (ArrayList<Integer>) parentList2.clone();

        while (v1Path.get((v1Path.size()-1)) != lca) {
            v1Path.remove(v1Path.size()-1);
        }
        while (v2Path.get(v2Path.size()-1) != lca) {
            v2Path.remove(v2Path.size()-1);
        }

        v2Path.remove(v2Path.indexOf(lca));



        //building PathInfo class for printing

        PathInfo best = new PathInfo();
        best.dist = totalDist;
        best.pred = lca;
        //printing the answer
        if(print){ printLCA(best,v1Path,v2Path,v1,v2); }

        return best.dist;
    }

    public void printLCA(PathInfo best, ArrayList v1Path, ArrayList v2Path, int v1, int v2){
        System.out.println( graphName + " Best lca " + v1 + " " + v2 + " Distance: " + best.dist + " Ancestor " + best.pred + " Path: " + reportPath(v1Path,v2Path) );
    }

    public int outcast(int[] v) {

        ArrayList<Integer> allSums = new ArrayList<>();
        for (int i=0; i<v.length; i++){
            int sum = 0;
            for (int j=0; j<this.numVertex; j++){
                sum +=lca(v[i],j,false);
            }
            allSums.add(sum);
        }

        int indexValue = allSums.indexOf(Collections.max(allSums));
        int outcast = v[indexValue];

        System.out.println( "The outcast of " + Arrays.toString( v ) + " is " + outcast );
        return outcast;

    }

    public static void main(String[] args) {
        Graph graph1 = new Graph();
        graph1.makeGraph( "digraph1.txt" );

        //graph1.lca(2,6,true);


        //System.out.println(graph.toString());
        int[] set1 = {7, 10, 2};
        int[] set2 = {7, 17, 5, 11, 4, 23};
        int[] set3 = {10, 17, 13};

        graph1.lca( 3, 7 , true);
        graph1.lca( 5, 6 ,true);
        graph1.lca( 9, 1 ,true);
        graph1.outcast( set1 );

        Graph graph2 = new Graph();
        graph2.makeGraph( "digraph2.txt" );
        //System.out.println(graph2.toString());
        graph2.lca( 3, 24 ,true);

        graph2.outcast( set3 );
        graph2.outcast( set2 );
        graph2.outcast( set1 );
    }
}