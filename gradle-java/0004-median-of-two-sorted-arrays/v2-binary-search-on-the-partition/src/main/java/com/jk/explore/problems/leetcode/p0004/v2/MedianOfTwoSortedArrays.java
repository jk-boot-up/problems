package com.jk.explore.problems.leetcode.p0004.v2;

import java.util.*;

public class MedianOfTwoSortedArrays {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] a = nums1.length <= nums2.length ? nums1 : nums2;
        int[] b = a == nums1 ? nums2 : nums1;
        int m = a.length, n = b.length, half = (m + n + 1) / 2, lo = 0, hi = m;
        while (true) {
            int i = (lo + hi) >>> 1, j = half - i;
            int aLeft = i == 0 ? Integer.MIN_VALUE : a[i - 1];
            int aRight = i == m ? Integer.MAX_VALUE : a[i];
            int bLeft = j == 0 ? Integer.MIN_VALUE : b[j - 1];
            int bRight = j == n ? Integer.MAX_VALUE : b[j];
            if (aLeft <= bRight && bLeft <= aRight) {
                int leftMax = Math.max(aLeft, bLeft);
                if ((m + n) % 2 == 1) return leftMax;
                return (leftMax + (double) Math.min(aRight, bRight)) / 2;
            }
            if (aLeft > bRight) hi = i - 1; else lo = i + 1;
        }
    }
}
