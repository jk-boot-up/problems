package com.jk.explore.problems.leetcode.p0852.v1;

import java.util.*;

public class PeakIndexInMountain {

    public int peakIndexInMountainArray(int[] arr) {
        int lo = 0, hi = arr.length - 1;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] < arr[mid + 1]) lo = mid + 1; else hi = mid;
        }
        return lo;
    }
}
