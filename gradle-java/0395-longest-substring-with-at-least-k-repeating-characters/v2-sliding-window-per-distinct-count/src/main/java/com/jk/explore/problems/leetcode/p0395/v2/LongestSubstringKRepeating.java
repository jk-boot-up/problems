package com.jk.explore.problems.leetcode.p0395.v2;

import java.util.*;

public class LongestSubstringKRepeating {

    public int longestSubstring(String s, int k) {
        int best = 0, n = s.length();
        for (int target = 1; target <= 26; target++) {
            int[] count = new int[26];
            int distinct = 0, atLeastK = 0;
            for (int lo = 0, hi = 0; hi < n; hi++) {
                int c = s.charAt(hi) - 'a';
                if (count[c]++ == 0) distinct++;
                if (count[c] == k) atLeastK++;
                while (distinct > target) {
                    int d = s.charAt(lo++) - 'a';
                    if (count[d]-- == k) atLeastK--;
                    if (count[d] == 0) distinct--;
                }
                if (distinct == target && atLeastK == target) best = Math.max(best, hi - lo + 1);
            }
        }
        return best;
    }
}
