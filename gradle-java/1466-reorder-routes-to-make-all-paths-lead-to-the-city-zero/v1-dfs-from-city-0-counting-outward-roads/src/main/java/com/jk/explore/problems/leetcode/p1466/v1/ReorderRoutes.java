package com.jk.explore.problems.leetcode.p1466.v1;

import java.util.*;

public class ReorderRoutes {

    public int minReorder(int n, int[][] connections) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int[] c : connections) {
            adj.get(c[0]).add(new int[]{c[1], 1}); // original direction: away from c[0]
            adj.get(c[1]).add(new int[]{c[0], 0});
        }
        boolean[] seen = new boolean[n];
        Deque<Integer> stack = new ArrayDeque<>(List.of(0));
        seen[0] = true;
        int flips = 0;
        while (!stack.isEmpty()) {
            int u = stack.pop();
            for (int[] e : adj.get(u)) {
                if (!seen[e[0]]) {
                    seen[e[0]] = true;
                    flips += e[1];
                    stack.push(e[0]);
                }
            }
        }
        return flips;
    }
}
