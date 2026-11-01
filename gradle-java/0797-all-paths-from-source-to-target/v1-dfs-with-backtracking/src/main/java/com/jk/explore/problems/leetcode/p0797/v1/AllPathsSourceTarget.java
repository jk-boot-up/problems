package com.jk.explore.problems.leetcode.p0797.v1;

import java.util.*;

public class AllPathsSourceTarget {

    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        List<List<Integer>> out = new ArrayList<>();
        List<Integer> path = new ArrayList<>(List.of(0));
        dfs(graph, 0, path, out);
        return out;
    }

    private void dfs(int[][] graph, int u, List<Integer> path, List<List<Integer>> out) {
        if (u == graph.length - 1) {
            out.add(new ArrayList<>(path));
            return;
        }
        for (int v : graph[u]) {
            path.add(v);
            dfs(graph, v, path, out);
            path.removeLast();
        }
    }
}
