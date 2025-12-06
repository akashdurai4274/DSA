package Java.Graph.Traversal;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class BFS {

    public static void main(String[] args) {
        int m = 9;
        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();

        for (int i = 0; i <= m; i++) {
            adj.add(new ArrayList<Integer>());
        }

        add_Edge(adj, 1, 2);
        add_Edge(adj, 1, 6);
        add_Edge(adj, 2, 3);
        add_Edge(adj, 2, 4);
        add_Edge(adj, 6, 7);
        add_Edge(adj, 6, 9);
        add_Edge(adj, 4, 5);
        add_Edge(adj, 7, 8);

        System.out.println(BFS_Traversal(adj));
    }

    public static void add_Edge(ArrayList<ArrayList<Integer>> adj, int u, int v) {
        adj.get(u).add(v);
        adj.get(v).add(u);
    }

    public static ArrayList<Integer> BFS_Traversal(ArrayList<ArrayList<Integer>> adj) {
        int V = adj.size();
        System.out.println(V);
        
        ArrayList<Integer> bfs = new ArrayList<>();
        boolean visited[] = new boolean[V];
        Queue<Integer> q = new LinkedList<>();

        q.add(1);
        visited[1] = true;

        while (!q.isEmpty()) {
            Integer node = q.poll();
            bfs.add(node);

            for (Integer it : adj.get(node)) {
                if (visited[it] == false) {
                    visited[it] = true;
                    q.add(it);
                }
            }
        }

        return bfs;
    }
}
