package com.jk.explore.problems.leetcode.p0041.v1;

import java.util.*;

public class FirstMissingPositive {

    public int firstMissingPositive(int[] nums) {
        int[] a = nums.clone();
        int n = a.length;
        for (int i = 0; i < n; i++) {
            while (a[i] >= 1 && a[i] <= n && a[a[i] - 1] != a[i]) {
                int j = a[i] - 1, t = a[j];
                a[j] = a[i];
                a[i] = t;
            }
        }
        for (int i = 0; i < n; i++) {
            if (a[i] != i + 1) return i + 1;
        }
        return n + 1;
    }
}
