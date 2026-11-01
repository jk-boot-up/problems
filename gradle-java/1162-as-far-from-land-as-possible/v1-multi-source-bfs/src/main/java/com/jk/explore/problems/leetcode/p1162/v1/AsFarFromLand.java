package com.jk.explore.problems.leetcode.p1162.v1;

import java.util.*;

public class AsFarFromLand {

    public int maxDistance(int[][] grid) {
        int n = grid.length;
        int[][] dist = new int[n][n];
        Deque<int[]> queue = new ArrayDeque<>();
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) queue.add(new int[]{r, c});
                else dist[r][c] = -1;
            }
        if (queue.isEmpty() || queue.size() == n * n) return -1;
        int best = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!queue.isEmpty()) {
            int[] p = queue.poll();
            for (int[] d : dirs) {
                int r = p[0] + d[0], c = p[1] + d[1];
                if (r < 0 || c < 0 || r >= n || c >= n || dist[r][c] != -1) continue;
                dist[r][c] = dist[p[0]][p[1]] + 1;
                best = Math.max(best, dist[r][c]);
                queue.add(new int[]{r, c});
            }
        }
        return best;
    }
}
