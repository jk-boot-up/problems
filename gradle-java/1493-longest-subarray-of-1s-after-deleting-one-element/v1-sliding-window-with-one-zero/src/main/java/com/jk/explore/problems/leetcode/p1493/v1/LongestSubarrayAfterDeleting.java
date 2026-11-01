package com.jk.explore.problems.leetcode.p1493.v1;

import java.util.*;

public class LongestSubarrayAfterDeleting {

    public int longestSubarray(int[] nums) {
        int left = 0, zeros = 0, best = 0;
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) zeros++;
            while (zeros > 1) {
                if (nums[left++] == 0) zeros--;
            }
            best = Math.max(best, right - left);
        }
        return best;
    }
}
