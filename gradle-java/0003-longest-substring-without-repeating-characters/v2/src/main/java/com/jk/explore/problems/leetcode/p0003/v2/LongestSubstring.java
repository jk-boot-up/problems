package com.jk.explore.problems.leetcode.p0003.v2;

import java.util.*;

public class LongestSubstring {

    public int lengthOfLongestSubstring(String s) {
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int left = 0, best = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (last[c] >= left) {
                left = last[c] + 1;
            }
            last[c] = right;
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
