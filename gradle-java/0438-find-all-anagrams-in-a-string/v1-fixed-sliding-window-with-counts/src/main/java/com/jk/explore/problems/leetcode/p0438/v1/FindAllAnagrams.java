package com.jk.explore.problems.leetcode.p0438.v1;

import java.util.*;

public class FindAllAnagrams {

    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> out = new ArrayList<>();
        if (p.length() > s.length()) return out;
        int[] need = new int[26];
        for (char c : p.toCharArray()) need[c - 'a']++;
        int diff = 0;
        for (int x : need) if (x != 0) diff++;
        for (int i = 0; i < s.length(); i++) {
            diff += change(need, s.charAt(i) - 'a', -1);
            if (i >= p.length()) diff += change(need, s.charAt(i - p.length()) - 'a', +1);
            if (i >= p.length() - 1 && diff == 0) out.add(i - p.length() + 1);
        }
        return out;
    }

    /** Applies delta to need[c] and returns how the number of non-zero entries changed. */
    private static int change(int[] need, int c, int delta) {
        int before = need[c] != 0 ? 1 : 0;
        need[c] += delta;
        return (need[c] != 0 ? 1 : 0) - before;
    }
}
