package com.jk.explore.problems.leetcode.p0567.v1;

import java.util.*;

public class PermutationInString {

    public boolean checkInclusion(String s1, String s2) {
        int k = s1.length();
        if (k > s2.length()) return false;
        int[] need = new int[26];
        for (char c : s1.toCharArray()) need[c - 'a']++;
        int zero = 0;
        for (int x : need) if (x == 0) zero++;
        for (int i = 0; i < s2.length(); i++) {
            zero += update(need, s2.charAt(i) - 'a', -1);
            if (i >= k) zero += update(need, s2.charAt(i - k) - 'a', +1);
            if (zero == 26) return true;
        }
        return false;
    }

    /** Applies delta and returns the change in the number of zero entries. */
    private static int update(int[] need, int c, int delta) {
        int before = need[c] == 0 ? 1 : 0;
        need[c] += delta;
        return (need[c] == 0 ? 1 : 0) - before;
    }
}
