package com.jk.explore.problems.leetcode.p0378.v1;

import java.util.*;

public class KthSmallestInMatrix {

    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> Integer.compare(matrix[a[0]][a[1]], matrix[b[0]][b[1]]));
        for (int r = 0; r < n; r++) heap.add(new int[]{r, 0});
        int[] cur = null;
        for (int i = 0; i < k; i++) {
            cur = heap.poll();
            if (cur[1] + 1 < n) heap.add(new int[]{cur[0], cur[1] + 1});
        }
        return matrix[cur[0]][cur[1]];
    }
}
