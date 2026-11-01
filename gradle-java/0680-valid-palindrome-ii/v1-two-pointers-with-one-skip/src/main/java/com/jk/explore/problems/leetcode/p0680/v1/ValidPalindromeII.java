package com.jk.explore.problems.leetcode.p0680.v1;

import java.util.*;

public class ValidPalindromeII {

    public boolean validPalindrome(String s) {
        for (int l = 0, r = s.length() - 1; l < r; l++, r--) {
            if (s.charAt(l) != s.charAt(r)) return isPalindrome(s, l + 1, r) || isPalindrome(s, l, r - 1);
        }
        return true;
    }

    private static boolean isPalindrome(String s, int l, int r) {
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}
