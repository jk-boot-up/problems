package com.jk.explore.problems.leetcode.p0556.v1;

import java.util.*;

public class NextGreaterElementIII {

    public int nextGreaterElement(int n) {
        char[] d = String.valueOf(n).toCharArray();
        int i = d.length - 2;
        while (i >= 0 && d[i] >= d[i + 1]) i--;
        if (i < 0) return -1;
        int j = d.length - 1;
        while (d[j] <= d[i]) j--;
        char t = d[i];
        d[i] = d[j];
        d[j] = t;
        for (int l = i + 1, r = d.length - 1; l < r; l++, r--) {
            t = d[l];
            d[l] = d[r];
            d[r] = t;
        }
        long value = Long.parseLong(new String(d));
        return value > Integer.MAX_VALUE ? -1 : (int) value;
    }
}
