package com.jk.explore.problems.leetcode.p0268.v1;

import java.util.*;

public class MissingNumber {

    public int missingNumber(int[] nums) {
        int n = nums.length, sum = n * (n + 1) / 2;
        for (int x : nums) sum -= x;
        return sum;
    }
}
