package com.jk.explore.problems.leetcode.p0973.v1;

import java.util.*;

public class KClosestPoints {

    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(dist(b), dist(a)));
        for (int[] p : points) {
            heap.add(p);
            if (heap.size() > k) heap.poll();
        }
        return heap.toArray(new int[0][]);
    }

    private static int dist(int[] p) {
        return p[0] * p[0] + p[1] * p[1];
    }
}
