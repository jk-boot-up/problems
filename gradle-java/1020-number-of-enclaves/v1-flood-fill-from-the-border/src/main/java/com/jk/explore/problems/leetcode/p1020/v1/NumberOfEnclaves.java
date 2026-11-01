package com.jk.explore.problems.leetcode.p1020.v1;

import java.util.*;

public class NumberOfEnclaves {

    public int numEnclaves(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        boolean[][] seen = new boolean[m][n];
        Deque<int[]> stack = new ArrayDeque<>();
        for (int r = 0; r < m; r++)
            for (int c = 0; c < n; c++)
                if ((r == 0 || c == 0 || r == m - 1 || c == n - 1) && grid[r][c] == 1) {
                    seen[r][c] = true;
                    stack.push(new int[]{r, c});
                }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] p = stack.pop();
            for (int[] d : dirs) {
                int r = p[0] + d[0], c = p[1] + d[1];
                if (r >= 0 && c >= 0 && r < m && c < n && grid[r][c] == 1 && !seen[r][c]) {
                    seen[r][c] = true;
                    stack.push(new int[]{r, c});
                }
            }
        }
        int count = 0;
        for (int r = 0; r < m; r++) for (int c = 0; c < n; c++) if (grid[r][c] == 1 && !seen[r][c]) count++;
        return count;
    }
}
