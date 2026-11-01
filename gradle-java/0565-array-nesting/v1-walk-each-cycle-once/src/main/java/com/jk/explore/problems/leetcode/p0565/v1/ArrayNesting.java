package com.jk.explore.problems.leetcode.p0565.v1;

import java.util.*;

public class ArrayNesting {

    public int arrayNesting(int[] nums) {
        int[] a = nums.clone();
        int best = 0;
        for (int i = 0; i < a.length; i++) {
            int len = 0;
            for (int j = i; a[j] != -1; len++) {
                int next = a[j];
                a[j] = -1;
                j = next;
            }
            best = Math.max(best, len);
        }
        return best;
    }
}
