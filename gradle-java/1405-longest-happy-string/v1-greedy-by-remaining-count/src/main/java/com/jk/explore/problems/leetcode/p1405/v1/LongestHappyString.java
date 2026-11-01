package com.jk.explore.problems.leetcode.p1405.v1;

import java.util.*;

public class LongestHappyString {

    public String longestDiverseString(int a, int b, int c) {
        int[] left = {a, b, c};
        StringBuilder sb = new StringBuilder();
        while (true) {
            Integer[] order = {0, 1, 2};
            Arrays.sort(order, (x, y) -> left[y] - left[x]);
            boolean placed = false;
            for (int i : order) {
                if (left[i] == 0) break;
                char ch = (char) ('a' + i);
                int n = sb.length();
                if (n >= 2 && sb.charAt(n - 1) == ch && sb.charAt(n - 2) == ch) continue;
                sb.append(ch);
                left[i]--;
                placed = true;
                break;
            }
            if (!placed) return sb.toString();
        }
    }
}
