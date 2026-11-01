package com.jk.explore.problems.leetcode.p0417.v1;

import java.util.*;

public class PacificAtlanticWaterFlow {

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        boolean[][] pac = new boolean[m][n], atl = new boolean[m][n];
        Deque<int[]> pq = new ArrayDeque<>(), aq = new ArrayDeque<>();
        for (int r = 0; r < m; r++) {
            mark(pac, pq, r, 0);
            mark(atl, aq, r, n - 1);
        }
        for (int c = 0; c < n; c++) {
            mark(pac, pq, 0, c);
            mark(atl, aq, m - 1, c);
        }
        bfs(heights, pac, pq);
        bfs(heights, atl, aq);
        List<List<Integer>> out = new ArrayList<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (pac[r][c] && atl[r][c]) out.add(List.of(r, c));
            }
        }
        return out;
    }

    private static void mark(boolean[][] seen, Deque<int[]> q, int r, int c) {
        if (!seen[r][c]) {
            seen[r][c] = true;
            q.add(new int[]{r, c});
        }
    }

    private static void bfs(int[][] h, boolean[][] seen, Deque<int[]> q) {
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            int[] cell = q.poll();
            for (int[] d : dirs) {
                int r = cell[0] + d[0], c = cell[1] + d[1];
                if (r >= 0 && r < h.length && c >= 0 && c < h[0].length && !seen[r][c] && h[r][c] >= h[cell[0]][cell[1]]) {
                    mark(seen, q, r, c);
                }
            }
        }
    }
}
