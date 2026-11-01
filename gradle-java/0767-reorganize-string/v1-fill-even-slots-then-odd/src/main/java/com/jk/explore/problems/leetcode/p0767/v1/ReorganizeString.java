package com.jk.explore.problems.leetcode.p0767.v1;

import java.util.*;

public class ReorganizeString {

    public String reorganizeString(String s) {
        int n = s.length();
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c - 'a']++;
        int top = 0;
        for (int c = 1; c < 26; c++) if (count[c] > count[top]) top = c;
        if (count[top] > (n + 1) / 2) return "";
        char[] out = new char[n];
        int pos = 0;
        for (int k = 0; k < 26; k++) {
            int c = k == 0 ? top : (k == top ? 0 : k);
            for (; count[c] > 0; count[c]--) {
                if (pos >= n) pos = 1;
                out[pos] = (char) ('a' + c);
                pos += 2;
            }
        }
        return new String(out);
    }
}
