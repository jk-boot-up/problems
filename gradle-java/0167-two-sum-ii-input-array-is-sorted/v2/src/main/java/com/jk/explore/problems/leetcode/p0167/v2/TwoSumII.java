package com.jk.explore.problems.leetcode.p0167.v2;

import java.util.*;

public class TwoSumII {

    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1;
        while (l < r) {
            int sum = numbers[l] + numbers[r];
            if (sum == target) {
                return new int[]{l + 1, r + 1};
            } else if (sum < target) {
                l++;
            } else {
                r--;
            }
        }
        throw new IllegalArgumentException("No solution");
    }
}
