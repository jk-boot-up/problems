package com.jk.explore.problems.leetcode.p0154.v1;

import java.util.*;

public class FindMinimumRotatedII {

    public int findMin(int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (nums[mid] > nums[hi]) lo = mid + 1;
            else if (nums[mid] < nums[hi]) hi = mid;
            else hi--;
        }
        return nums[lo];
    }
}
