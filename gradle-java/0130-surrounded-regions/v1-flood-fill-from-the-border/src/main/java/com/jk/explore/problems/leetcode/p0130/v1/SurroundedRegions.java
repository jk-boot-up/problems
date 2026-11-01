package com.jk.explore.problems.leetcode.p0130.v1;

import java.util.*;

public class SurroundedRegions {

    public void solve(char[][] board) {
        int m = board.length, n = board[0].length;
        Deque<int[]> stack = new ArrayDeque<>();
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if ((r == 0 || c == 0 || r == m - 1 || c == n - 1) && board[r][c] == 'O') {
                    board[r][c] = '#';
                    stack.push(new int[]{r, c});
                }
            }
        }
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] cell = stack.pop();
            for (int[] d : dirs) {
                int nr = cell[0] + d[0], nc = cell[1] + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && board[nr][nc] == 'O') {
                    board[nr][nc] = '#';
                    stack.push(new int[]{nr, nc});
                }
            }
        }
        for (char[] row : board) {
            for (int c = 0; c < n; c++) {
                row[c] = row[c] == '#' ? 'O' : 'X';
            }
        }
    }
}
