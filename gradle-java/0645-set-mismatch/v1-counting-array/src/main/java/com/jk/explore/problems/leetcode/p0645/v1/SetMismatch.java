package com.jk.explore.problems.leetcode.p0645.v1;

import java.util.*;

public class SetMismatch {

    public int[] findErrorNums(int[] nums) {
        int n = nums.length, dup = -1, missing = -1;
        int[] count = new int[n + 1];
        for (int x : nums) count[x]++;
        for (int v = 1; v <= n; v++) {
            if (count[v] == 2) dup = v;
            if (count[v] == 0) missing = v;
        }
        return new int[]{dup, missing};
    }
}
