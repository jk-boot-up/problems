package com.jk.explore.problems.leetcode.p0395.v1;

import java.util.*;

public class LongestSubstringKRepeating {

    public int longestSubstring(String s, int k) {
        return solve(s, 0, s.length(), k);
    }

    private int solve(String s, int lo, int hi, int k) {
        if (hi - lo < k) return 0;
        int[] count = new int[26];
        for (int i = lo; i < hi; i++) count[s.charAt(i) - 'a']++;
        int best = 0, start = lo;
        boolean split = false;
        for (int i = lo; i < hi; i++) {
            if (count[s.charAt(i) - 'a'] < k) {
                split = true;
                best = Math.max(best, solve(s, start, i, k));
                start = i + 1;
            }
        }
        if (!split) return hi - lo;
        return Math.max(best, solve(s, start, hi, k));
    }
}
