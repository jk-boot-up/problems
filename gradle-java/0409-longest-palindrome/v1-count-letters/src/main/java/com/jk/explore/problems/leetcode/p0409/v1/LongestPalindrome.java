package com.jk.explore.problems.leetcode.p0409.v1;

import java.util.*;

public class LongestPalindrome {

    public int longestPalindrome(String s) {
        int[] count = new int[128];
        for (char c : s.toCharArray()) count[c]++;
        int length = 0;
        boolean odd = false;
        for (int c : count) {
            length += c / 2 * 2;
            if (c % 2 == 1) odd = true;
        }
        return length + (odd ? 1 : 0);
    }
}
