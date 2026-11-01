package com.jk.explore.problems.leetcode.p0785.v1;

import java.util.*;

public class IsGraphBipartite {

    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n]; // 0 = uncoloured, 1 / -1 = the two sides
        for (int s = 0; s < n; s++) {
            if (color[s] != 0) continue;
            color[s] = 1;
            Deque<Integer> queue = new ArrayDeque<>(List.of(s));
            while (!queue.isEmpty()) {
                int u = queue.poll();
                for (int v : graph[u]) {
                    if (color[v] == color[u]) return false;
                    if (color[v] == 0) {
                        color[v] = -color[u];
                        queue.add(v);
                    }
                }
            }
        }
        return true;
    }
}
