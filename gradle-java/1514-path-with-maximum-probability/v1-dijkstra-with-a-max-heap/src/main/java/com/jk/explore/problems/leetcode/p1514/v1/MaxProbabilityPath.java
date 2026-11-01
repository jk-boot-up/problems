package com.jk.explore.problems.leetcode.p1514.v1;

import java.util.*;

public class MaxProbabilityPath {

    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        int m = edges.length;
        int[] head = new int[n], next = new int[2 * m], to = new int[2 * m];
        double[] prob = new double[2 * m];
        Arrays.fill(head, -1);
        for (int i = 0; i < m; i++)
            for (int side = 0; side < 2; side++) {
                int e = 2 * i + side, u = edges[i][side], v = edges[i][1 - side];
                to[e] = v;
                prob[e] = succProb[i];
                next[e] = head[u];
                head[u] = e;
            }
        double[] best = new double[n];
        best[start] = 1;
        PriorityQueue<double[]> heap = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
        heap.add(new double[]{1, start});
        while (!heap.isEmpty()) {
            double[] top = heap.poll();
            int u = (int) top[1];
            if (top[0] < best[u]) continue;
            if (u == end) return top[0];
            for (int e = head[u]; e != -1; e = next[e]) {
                double p = top[0] * prob[e];
                if (p > best[to[e]]) {
                    best[to[e]] = p;
                    heap.add(new double[]{p, to[e]});
                }
            }
        }
        return 0;
    }
}
