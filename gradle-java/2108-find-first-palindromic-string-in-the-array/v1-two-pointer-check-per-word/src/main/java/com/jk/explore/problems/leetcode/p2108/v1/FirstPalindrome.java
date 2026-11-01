package com.jk.explore.problems.leetcode.p2108.v1;

import java.util.*;

public class FirstPalindrome {

    public String firstPalindrome(String[] words) {
        for (String w : words) if (isPalindrome(w)) return w;
        return "";
    }

    private boolean isPalindrome(String w) {
        for (int i = 0, j = w.length() - 1; i < j; i++, j--) if (w.charAt(i) != w.charAt(j)) return false;
        return true;
    }
}
