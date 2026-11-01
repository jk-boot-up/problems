package com.jk.explore.problems.leetcode.p0200.v1;

import java.util.*;

public class NumberOfIslands {

    public int numIslands(char[][] grid) {
        int m = grid.length, n = grid[0].length, islands = 0;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] != '1') continue;
                islands++;
                Deque<int[]> queue = new ArrayDeque<>();
                queue.add(new int[]{r, c});
                grid[r][c] = '0';
                while (!queue.isEmpty()) {
                    int[] cell = queue.poll();
                    for (int[] d : dirs) {
                        int nr = cell[0] + d[0], nc = cell[1] + d[1];
                        if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == '1') {
                            grid[nr][nc] = '0';
                            queue.add(new int[]{nr, nc});
                        }
                    }
                }
            }
        }
        return islands;
    }
}
