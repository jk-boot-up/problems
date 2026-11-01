package com.jk.explore.problems.leetcode.p0215.v3;

import java.util.*;

public class KthLargest {

    private final Random random = new Random(42);

    public int findKthLargest(int[] nums, int k) {
        int[] a = nums.clone();
        int target = a.length - k, lo = 0, hi = a.length - 1;
        while (true) {
            int pivot = a[lo + random.nextInt(hi - lo + 1)];
            int lt = lo, i = lo, gt = hi; // a[lo..lt-1] < pivot, a[lt..i-1] == pivot, a[gt+1..hi] > pivot
            while (i <= gt) {
                if (a[i] < pivot) swap(a, lt++, i++);
                else if (a[i] > pivot) swap(a, i, gt--);
                else i++;
            }
            if (target < lt) hi = lt - 1;
            else if (target > gt) lo = gt + 1;
            else return pivot;
        }
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
