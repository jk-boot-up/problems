package com.jk.explore.problems.leetcode.p1456.v1;

import java.util.*;

public class MaxVowels {

    private static int v(char c) {
        return "aeiou".indexOf(c) >= 0 ? 1 : 0;
    }

    public int maxVowels(String s, int k) {
        int count = 0, best = 0;
        for (int i = 0; i < s.length(); i++) {
            count += v(s.charAt(i));
            if (i >= k) count -= v(s.charAt(i - k));
            best = Math.max(best, count);
        }
        return best;
    }
}
