package com.jk.explore.problems.leetcode.p0454.v1;

import java.util.*;

public class FourSumII {

    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        int count = 0;
        for (int a : nums1) for (int b : nums2) for (int c : nums3) for (int d : nums4) if (a + b + c + d == 0) count++;
        return count;
    }
}
