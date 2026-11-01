package com.jk.explore.problems.leetcode.p0034.v1;

import java.util.*;

public class FirstAndLastPosition {

    public int[] searchRange(int[] nums, int target) {
        int first = lower(nums, target);
        if (first == nums.length || nums[first] != target) return new int[]{-1, -1};
        return new int[]{first, lower(nums, (long) target + 1) - 1};
    }

    private static int lower(int[] nums, long x) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] < x) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
