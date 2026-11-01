package com.jk.explore.problems.leetcode.p0087.v1;

import java.util.*;

public class ScrambleString {

    private final MyHashMap<String, Boolean> memo = new MyHashMap<>();

    public boolean isScramble(String s1, String s2) {
        if (s1.equals(s2)) return true;
        String key = s1 + "#" + s2;
        Boolean cached = memo.get(key);
        if (cached != null) return cached;
        int n = s1.length();
        int[] count = new int[26];
        for (int i = 0; i < n; i++) {
            count[s1.charAt(i) - 'a']++;
            count[s2.charAt(i) - 'a']--;
        }
        boolean result = false;
        for (int c : count) {
            if (c != 0) {
                memo.put(key, false);
                return false;
            }
        }
        for (int k = 1; k < n && !result; k++) {
            result = (isScramble(s1.substring(0, k), s2.substring(0, k)) && isScramble(s1.substring(k), s2.substring(k)))
                    || (isScramble(s1.substring(0, k), s2.substring(n - k)) && isScramble(s1.substring(k), s2.substring(0, n - k)));
        }
        memo.put(key, result);
        return result;
    }
}
