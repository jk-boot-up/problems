package com.jk.explore.problems.leetcode.p0005.v1;

import java.util.*;

public class LongestPalindromicSubstring {

    public String longestPalindrome(String s) {
        int n = s.length(), bestStart = 0, bestLen = 1;
        boolean[][] pal = new boolean[n][n];
        for (int len = 1; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                pal[i][j] = s.charAt(i) == s.charAt(j) && (len < 3 || pal[i + 1][j - 1]);
                if (pal[i][j] && len > bestLen) {
                    bestLen = len;
                    bestStart = i;
                }
            }
        }
        return s.substring(bestStart, bestStart + bestLen);
    }
}
