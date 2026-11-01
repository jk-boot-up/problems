package com.jk.explore.problems.leetcode.p1584.v1;

import java.util.*;

public class MinCostConnectPoints {

    public int minCostConnectPoints(int[][] points) {
        int n = points.length, total = 0;
        int[] best = new int[n];
        boolean[] inTree = new boolean[n];
        Arrays.fill(best, Integer.MAX_VALUE);
        best[0] = 0;
        for (int round = 0; round < n; round++) {
            int u = -1;
            for (int i = 0; i < n; i++) {
                if (!inTree[i] && (u < 0 || best[i] < best[u])) u = i;
            }
            inTree[u] = true;
            total += best[u];
            for (int v = 0; v < n; v++) {
                if (!inTree[v]) {
                    int d = Math.abs(points[u][0] - points[v][0]) + Math.abs(points[u][1] - points[v][1]);
                    if (d < best[v]) best[v] = d;
                }
            }
        }
        return total;
    }
}
