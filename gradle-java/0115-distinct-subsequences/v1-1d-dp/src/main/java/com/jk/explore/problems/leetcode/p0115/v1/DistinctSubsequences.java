package com.jk.explore.problems.leetcode.p0115.v1;

import java.util.*;

public class DistinctSubsequences {

    public int numDistinct(String s, String t) {
        int n = t.length();
        long[] ways = new long[n + 1];
        ways[0] = 1;
        for (char c : s.toCharArray()) {
            for (int j = n; j >= 1; j--) {
                if (t.charAt(j - 1) == c) ways[j] += ways[j - 1];
            }
        }
        return (int) ways[n];
    }
}
