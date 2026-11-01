package com.jk.explore.problems.leetcode.p0218.v2;

import java.util.*;

public class Skyline {

    public List<List<Integer>> getSkyline(int[][] buildings) {
        int m = buildings.length;
        int[] xs = new int[2 * m];
        for (int i = 0; i < m; i++) {
            xs[2 * i] = buildings[i][0];
            xs[2 * i + 1] = buildings[i][1];
        }
        Arrays.sort(xs);
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(b[0], a[0]));
        List<List<Integer>> out = new ArrayList<>();
        int next = 0;
        for (int k = 0; k < xs.length; k++) {
            int x = xs[k];
            if (k > 0 && x == xs[k - 1]) continue;
            while (next < m && buildings[next][0] <= x) {
                heap.add(new int[]{buildings[next][2], buildings[next][1]});
                next++;
            }
            while (!heap.isEmpty() && heap.peek()[1] <= x) heap.poll();
            int h = heap.isEmpty() ? 0 : heap.peek()[0];
            if (out.isEmpty() || out.get(out.size() - 1).get(1) != h) out.add(List.of(x, h));
        }
        return out;
    }
}
