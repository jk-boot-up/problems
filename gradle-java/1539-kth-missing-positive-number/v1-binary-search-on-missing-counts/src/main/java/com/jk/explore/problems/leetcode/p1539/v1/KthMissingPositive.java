package com.jk.explore.problems.leetcode.p1539.v1;

import java.util.*;

public class KthMissingPositive {

    public int findKthPositive(int[] arr, int k) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] - mid - 1 < k) lo = mid + 1;
            else hi = mid;
        }
        return lo + k;
    }
}
