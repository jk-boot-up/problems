package com.jk.explore.problems.leetcode.p0085.v1;

import java.util.*;

public class MaximalRectangle {

    public int maximalRectangle(char[][] matrix) {
        int n = matrix[0].length, best = 0;
        int[] heights = new int[n];
        for (char[] row : matrix) {
            for (int c = 0; c < n; c++) heights[c] = row[c] == '1' ? heights[c] + 1 : 0;
            best = Math.max(best, largest(heights));
        }
        return best;
    }

    private static int largest(int[] h) {
        Deque<Integer> stack = new ArrayDeque<>();
        int best = 0;
        for (int i = 0; i <= h.length; i++) {
            int cur = i == h.length ? 0 : h[i];
            while (!stack.isEmpty() && h[stack.peek()] > cur) {
                int height = h[stack.pop()];
                int left = stack.isEmpty() ? -1 : stack.peek();
                best = Math.max(best, height * (i - left - 1));
            }
            stack.push(i);
        }
        return best;
    }
}
