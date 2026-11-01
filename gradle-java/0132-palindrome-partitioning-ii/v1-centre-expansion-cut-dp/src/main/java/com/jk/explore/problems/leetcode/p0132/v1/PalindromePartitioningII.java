package com.jk.explore.problems.leetcode.p0132.v1;

import java.util.*;

public class PalindromePartitioningII {

    public int minCut(String s) {
        int n = s.length();
        int[] cuts = new int[n + 1];
        for (int i = 0; i <= n; i++) cuts[i] = i - 1;
        for (int c = 0; c < n; c++) {
            for (int l = c, r = c; l >= 0 && r < n && s.charAt(l) == s.charAt(r); l--, r++) cuts[r + 1] = Math.min(cuts[r + 1], cuts[l] + 1);
            for (int l = c, r = c + 1; l >= 0 && r < n && s.charAt(l) == s.charAt(r); l--, r++) cuts[r + 1] = Math.min(cuts[r + 1], cuts[l] + 1);
        }
        return cuts[n];
    }
}
