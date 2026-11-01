package com.jk.explore.problems.leetcode.p0743.v1;

import java.util.*;

public class NetworkDelayTime {

    public int networkDelayTime(int[][] times, int n, int k) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] t : times) graph.get(t[0]).add(new int[]{t[1], t[2]});
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        heap.add(new int[]{k, 0});
        int settled = 0, latest = 0;
        boolean[] done = new boolean[n + 1];
        while (!heap.isEmpty()) {
            int[] cur = heap.poll();
            int u = cur[0];
            if (done[u]) continue;
            done[u] = true;
            settled++;
            latest = cur[1];
            for (int[] e : graph.get(u)) {
                if (cur[1] + e[1] < dist[e[0]]) {
                    dist[e[0]] = cur[1] + e[1];
                    heap.add(new int[]{e[0], dist[e[0]]});
                }
            }
        }
        return settled == n ? latest : -1;
    }
}
