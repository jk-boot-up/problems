package com.jk.explore.problems.leetcode.p0005.v2;

import java.util.*;

public class LongestPalindromicSubstring {

    public String longestPalindrome(String s) {
        int bestStart = 0, bestLen = 0;
        for (int center = 0; center < 2 * s.length() - 1; center++) {
            int l = center / 2, r = l + center % 2;
            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                l--;
                r++;
            }
            if (r - l - 1 > bestLen) {
                bestLen = r - l - 1;
                bestStart = l + 1;
            }
        }
        return s.substring(bestStart, bestStart + bestLen);
    }
}
