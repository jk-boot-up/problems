package com.jk.explore.problems.leetcode.p0215.v1;

import java.util.*;

public class KthLargest {

    public int findKthLargest(int[] nums, int k) {
        int[] a = nums.clone();
        Arrays.sort(a);
        return a[a.length - k];
    }
}
