package com.jk.explore.problems.leetcode.p0977.v1;

import java.util.*;

public class SquaresOfSortedArray {

    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] out = new int[n];
        for (int l = 0, r = n - 1, k = n - 1; k >= 0; k--) {
            if (Math.abs(nums[l]) > Math.abs(nums[r])) out[k] = nums[l] * nums[l++];
            else out[k] = nums[r] * nums[r--];
        }
        return out;
    }
}
