package com.jk.explore.problems.leetcode.p0787.v1;

import java.util.*;

public class CheapestFlights {

    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        int inf = Integer.MAX_VALUE;
        int[] cost = new int[n];
        Arrays.fill(cost, inf);
        cost[src] = 0;
        for (int round = 0; round <= k; round++) {
            int[] next = cost.clone();
            for (int[] f : flights) {
                if (cost[f[0]] != inf && cost[f[0]] + f[2] < next[f[1]]) next[f[1]] = cost[f[0]] + f[2];
            }
            cost = next;
        }
        return cost[dst] == inf ? -1 : cost[dst];
    }
}
