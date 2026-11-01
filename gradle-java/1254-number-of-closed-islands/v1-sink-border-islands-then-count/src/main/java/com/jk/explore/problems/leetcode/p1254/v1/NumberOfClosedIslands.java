package com.jk.explore.problems.leetcode.p1254.v1;

import java.util.*;

public class NumberOfClosedIslands {

    public int closedIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] g = new int[m][];
        for (int r = 0; r < m; r++) g[r] = grid[r].clone();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if ((r == 0 || c == 0 || r == m - 1 || c == n - 1) && g[r][c] == 0) sink(g, r, c);
        int count = 0;
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if (g[r][c] == 0) {
                    count++;
                    sink(g, r, c);
                }
        return count;
    }

    private void sink(int[][] g, int r0, int c0) {
        Deque<int[]> stack = new ArrayDeque<>();
        g[r0][c0] = 1;
        stack.push(new int[]{r0, c0});
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] p = stack.pop();
            for (int[] d : dirs) {
                int r = p[0] + d[0], c = p[1] + d[1];
                if (r >= 0 && c >= 0 && r < g.length && c < g[0].length && g[r][c] == 0) {
                    g[r][c] = 1;
                    stack.push(new int[]{r, c});
                }
            }
        }
    }
}
