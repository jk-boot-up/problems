package com.jk.explore.problems.leetcode.p1926.v1;

import java.util.*;

public class NearestExit {

    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length, n = maze[0].length;
        boolean[][] seen = new boolean[m][n];
        Deque<int[]> queue = new ArrayDeque<>();
        queue.add(entrance);
        seen[entrance[0]][entrance[1]] = true;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int steps = 0; !queue.isEmpty(); steps++) {
            for (int size = queue.size(); size > 0; size--) {
                int[] c = queue.poll();
                boolean border = c[0] == 0 || c[1] == 0 || c[0] == m - 1 || c[1] == n - 1;
                if (border && steps > 0) return steps;
                for (int[] d : dirs) {
                    int r = c[0] + d[0], k = c[1] + d[1];
                    if (r >= 0 && r < m && k >= 0 && k < n && maze[r][k] == '.' && !seen[r][k]) {
                        seen[r][k] = true;
                        queue.add(new int[]{r, k});
                    }
                }
            }
        }
        return -1;
    }
}
