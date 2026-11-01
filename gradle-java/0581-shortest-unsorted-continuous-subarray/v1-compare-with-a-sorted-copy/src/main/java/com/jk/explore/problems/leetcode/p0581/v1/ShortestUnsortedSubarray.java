package com.jk.explore.problems.leetcode.p0581.v1;

import java.util.*;

public class ShortestUnsortedSubarray {

    public int findUnsortedSubarray(int[] nums) {
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi && nums[lo] == sorted[lo]) lo++;
        while (hi >= lo && nums[hi] == sorted[hi]) hi--;
        return hi - lo + 1;
    }
}
