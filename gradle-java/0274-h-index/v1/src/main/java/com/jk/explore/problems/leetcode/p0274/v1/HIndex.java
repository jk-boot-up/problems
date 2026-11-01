package com.jk.explore.problems.leetcode.p0274.v1;

import java.util.*;

public class HIndex {

    public int hIndex(int[] citations) {
        int[] c = citations.clone();
        Arrays.sort(c);
        int n = c.length, h = 0;
        while (h < n && c[n - 1 - h] > h) {
            h++;
        }
        return h;
    }
}
