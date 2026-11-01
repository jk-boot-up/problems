package com.jk.explore.problems.leetcode.p0778.v1;

import java.util.*;

public class SwimInRisingWater {

    public int swimInWater(int[][] grid) {
        int n = grid.length;
        boolean[][] seen = new boolean[n][n];
        PriorityQueue<int[]> heap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        heap.add(new int[]{grid[0][0], 0, 0});
        seen[0][0] = true;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (true) {
            int[] cur = heap.poll();
            if (cur[1] == n - 1 && cur[2] == n - 1) return cur[0];
            for (int[] d : dirs) {
                int r = cur[1] + d[0], c = cur[2] + d[1];
                if (r >= 0 && r < n && c >= 0 && c < n && !seen[r][c]) {
                    seen[r][c] = true;
                    heap.add(new int[]{Math.max(cur[0], grid[r][c]), r, c});
                }
            }
        }
    }
}
