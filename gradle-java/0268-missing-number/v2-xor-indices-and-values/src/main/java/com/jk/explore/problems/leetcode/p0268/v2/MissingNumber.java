package com.jk.explore.problems.leetcode.p0268.v2;

import java.util.*;

public class MissingNumber {

    public int missingNumber(int[] nums) {
        int x = nums.length;
        for (int i = 0; i < nums.length; i++) x ^= i ^ nums[i];
        return x;
    }
}
