package com.jk.explore.problems.leetcode.p0300.v1;

import java.util.*;

public class LongestIncreasingSubsequence {

    public int lengthOfLIS(int[] nums) {
        int n = nums.length, best = 0;
        int[] len = new int[n];
        for (int i = 0; i < n; i++) {
            len[i] = 1;
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) len[i] = Math.max(len[i], len[j] + 1);
            }
            best = Math.max(best, len[i]);
        }
        return best;
    }
}
