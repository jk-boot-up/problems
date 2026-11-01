package com.jk.explore.problems.leetcode.p0557.v1;

import java.util.*;

public class ReverseWordsIII {

    public String reverseWords(String s) {
        char[] a = s.toCharArray();
        for (int start = 0; start < a.length; ) {
            int end = start;
            while (end < a.length && a[end] != ' ') end++;
            for (int l = start, r = end - 1; l < r; l++, r--) {
                char t = a[l];
                a[l] = a[r];
                a[r] = t;
            }
            start = end + 1;
        }
        return new String(a);
    }
}
