package com.jk.explore.problems.leetcode.p0912.v2;

import java.util.*;

public class SortAnArray {

    public int[] sortArray(int[] nums) {
        int[] a = nums.clone();
        sort(a, new int[a.length], 0, a.length - 1);
        return a;
    }

    private void sort(int[] a, int[] buf, int lo, int hi) {
        if (lo >= hi) return;
        int mid = (lo + hi) >>> 1;
        sort(a, buf, lo, mid);
        sort(a, buf, mid + 1, hi);
        int i = lo, j = mid + 1, k = lo;
        while (i <= mid && j <= hi) buf[k++] = a[i] <= a[j] ? a[i++] : a[j++];
        while (i <= mid) buf[k++] = a[i++];
        while (j <= hi) buf[k++] = a[j++];
        System.arraycopy(buf, lo, a, lo, hi - lo + 1);
    }
}
