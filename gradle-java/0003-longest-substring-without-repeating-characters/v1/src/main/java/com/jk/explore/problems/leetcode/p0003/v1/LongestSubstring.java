package com.jk.explore.problems.leetcode.p0003.v1;

import java.util.*;

public class LongestSubstring {

    public int lengthOfLongestSubstring(String s) {
        Set<Character> window = new HashSet<>();
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            while (window.contains(c)) {
                window.remove(s.charAt(left++));
            }
            window.add(c);
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
