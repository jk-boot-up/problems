package com.jk.explore.problems.leetcode.p0695.v1;

import java.util.*;

public class MaxAreaOfIsland {

    public int maxAreaOfIsland(int[][] grid) {
        int m = grid.length, n = grid[0].length, best = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] != 1) continue;
                int area = 0;
                Deque<int[]> stack = new ArrayDeque<>();
                stack.push(new int[]{r, c});
                grid[r][c] = 0;
                while (!stack.isEmpty()) {
                    int[] cell = stack.pop();
                    area++;
                    for (int[] d : dirs) {
                        int a = cell[0] + d[0], b = cell[1] + d[1];
                        if (a >= 0 && a < m && b >= 0 && b < n && grid[a][b] == 1) {
                            grid[a][b] = 0;
                            stack.push(new int[]{a, b});
                        }
                    }
                }
                best = Math.max(best, area);
            }
        }
        return best;
    }
}
