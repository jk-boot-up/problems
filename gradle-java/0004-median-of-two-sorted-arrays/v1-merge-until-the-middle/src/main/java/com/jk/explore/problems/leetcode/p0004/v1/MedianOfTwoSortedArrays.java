package com.jk.explore.problems.leetcode.p0004.v1;

import java.util.*;

public class MedianOfTwoSortedArrays {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int total = nums1.length + nums2.length, i = 0, j = 0, prev = 0, cur = 0;
        for (int k = 0; k <= total / 2; k++) {
            prev = cur;
            if (j >= nums2.length || (i < nums1.length && nums1[i] <= nums2[j])) cur = nums1[i++];
            else cur = nums2[j++];
        }
        return total % 2 == 1 ? cur : (prev + (double) cur) / 2;
    }
}
