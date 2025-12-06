package Java.Graph.Traversal;

import java.util.ArrayList;

public class DFS {

    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<ArrayList<Integer>>();
        int m = 8;
        for (int i = 0; i <= m; i++) {
            adj.add(new ArrayList<Integer>());
        }
        add_Edges(adj, 1, 2);
        add_Edges(adj, 1, 3);
        add_Edges(adj, 2, 5);
        add_Edges(adj, 2, 6);
        add_Edges(adj, 3, 7);
        add_Edges(adj, 3, 4);
        add_Edges(adj, 4, 8);
        add_Edges(adj, 7, 8);

        System.out.println(DFS_starter(adj.size(), adj));
    }

    public static void add_Edges(ArrayList<ArrayList<Integer>> adj, int u, int v) {
        adj.get(u).add(v);
        adj.get(v).add(u);
    }

    public static ArrayList<Integer> DFS_starter(int V, ArrayList<ArrayList<Integer>> adj) {
        boolean[] visited = new boolean[V + 1];
        visited[0] = true;
        ArrayList<Integer> list = new ArrayList<>();
        DFS_Traversal(1, adj, visited, list);
        return list;
    }

    public static void DFS_Traversal(int node, ArrayList<ArrayList<Integer>> adj, boolean[] visited, ArrayList<Integer> list) {
        visited[node] = true;
        list.add(node);

        for (Integer it : adj.get(node)) {
            if (visited[it] == false) {
                DFS_Traversal(it, adj, visited, list);
            }
        }
    }
}
