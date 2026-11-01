package com.jk.explore.problems.leetcode.p0459.v2;

import java.util.*;

public class RepeatedSubstringPattern {

    public boolean repeatedSubstringPattern(String s) {
        int n = s.length();
        int[] lps = new int[n];
        for (int i = 1, len = 0; i < n; ) {
            if (s.charAt(i) == s.charAt(len)) lps[i++] = ++len;
            else if (len > 0) len = lps[len - 1];
            else lps[i++] = 0;
        }
        int border = lps[n - 1];
        return border > 0 && n % (n - border) == 0;
    }
}
