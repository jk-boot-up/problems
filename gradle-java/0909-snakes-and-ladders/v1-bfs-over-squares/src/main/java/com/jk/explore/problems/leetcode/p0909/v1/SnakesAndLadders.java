package com.jk.explore.problems.leetcode.p0909.v1;

import java.util.*;

public class SnakesAndLadders {

    public int snakesAndLadders(int[][] board) {
        int n = board.length, target = n * n;
        int[] dist = new int[target + 1];
        Arrays.fill(dist, -1);
        dist[1] = 0;
        Deque<Integer> queue = new ArrayDeque<>(List.of(1));
        while (!queue.isEmpty()) {
            int s = queue.poll();
            if (s == target) return dist[s];
            for (int next = s + 1; next <= Math.min(s + 6, target); next++) {
                int r = n - 1 - (next - 1) / n, c = (next - 1) % n;
                if ((n - 1 - r) % 2 == 1) c = n - 1 - c;
                int dest = board[r][c] == -1 ? next : board[r][c];
                if (dist[dest] == -1) {
                    dist[dest] = dist[s] + 1;
                    queue.add(dest);
                }
            }
        }
        return -1;
    }
}
