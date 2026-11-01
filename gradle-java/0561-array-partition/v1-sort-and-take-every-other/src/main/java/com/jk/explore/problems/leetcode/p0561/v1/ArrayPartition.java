package com.jk.explore.problems.leetcode.p0561.v1;

import java.util.*;

public class ArrayPartition {

    public int arrayPairSum(int[] nums) {
        int[] a = nums.clone();
        Arrays.sort(a);
        int sum = 0;
        for (int i = 0; i < a.length; i += 2) sum += a[i];
        return sum;
    }
}
