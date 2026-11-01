package com.jk.explore.problems.leetcode.p0009.v1;

import java.util.*;

public class PalindromeNumber {

    public boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        for (int i = 0, j = s.length() - 1; i < j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) return false;
        }
        return true;
    }
}
