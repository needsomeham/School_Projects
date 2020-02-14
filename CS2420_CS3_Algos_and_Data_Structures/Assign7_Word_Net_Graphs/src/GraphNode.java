import java.util.LinkedList;
import java.util.ArrayList;


public class GraphNode {

    public GraphNode( ){
        this.nodeID = 0;
        this.p2 = new PathInfo();
        this.p1 = new PathInfo();
        this.succ = new ArrayList<EdgeInfo>();
    }

    public GraphNode(  int nodeID){
        this.nodeID = nodeID;
        this.p2 = new PathInfo();
        this.p1 = new PathInfo();
        this.succ = new ArrayList<EdgeInfo>();
    }

    public String toString(){
        StringBuilder sb = new StringBuilder();
        sb.append(nodeID);
        sb.append(p1.toString());
        sb.append(p2.toString());
        for (EdgeInfo e:succ){
            sb.append(e.toString());
        }
        sb.append("\n");
        return sb.toString();
    }

    public void addEdge(int v1, int v2){
        succ.add( new EdgeInfo(v1,v2) );
    }

    public int nodeID;
    PathInfo p1;
    PathInfo p2;
   public ArrayList<EdgeInfo> succ;


}
