package com.jk.explore.problems.leetcode.p0345.v1;

import java.util.*;

public class ReverseVowels {

    private static boolean vowel(char c) {
        return "aeiouAEIOU".indexOf(c) >= 0;
    }

    public String reverseVowels(String s) {
        char[] a = s.toCharArray();
        for (int l = 0, r = a.length - 1; l < r; ) {
            if (!vowel(a[l])) l++;
            else if (!vowel(a[r])) r--;
            else {
                char t = a[l];
                a[l++] = a[r];
                a[r--] = t;
            }
        }
        return new String(a);
    }
}
