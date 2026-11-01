package com.jk.explore.problems.leetcode.p0525.v1;

import java.util.*;

public class ContiguousArray {

    public int findMaxLength(int[] nums) {
        int n = nums.length, balance = n, best = 0;
        int[] first = new int[2 * n + 1];
        Arrays.fill(first, -2);
        first[n] = -1;
        for (int i = 0; i < n; i++) {
            balance += nums[i] == 1 ? 1 : -1;
            if (first[balance] == -2) first[balance] = i;
            else best = Math.max(best, i - first[balance]);
        }
        return best;
    }
}
