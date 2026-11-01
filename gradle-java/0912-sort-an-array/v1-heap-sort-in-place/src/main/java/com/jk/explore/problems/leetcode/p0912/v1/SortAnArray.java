package com.jk.explore.problems.leetcode.p0912.v1;

import java.util.*;

public class SortAnArray {

    public int[] sortArray(int[] nums) {
        int[] a = nums.clone();
        int n = a.length;
        for (int i = n / 2 - 1; i >= 0; i--) siftDown(a, i, n);
        for (int end = n - 1; end > 0; end--) {
            swap(a, 0, end);
            siftDown(a, 0, end);
        }
        return a;
    }

    private static void siftDown(int[] a, int i, int n) {
        while (true) {
            int largest = i, l = 2 * i + 1, r = l + 1;
            if (l < n && a[l] > a[largest]) largest = l;
            if (r < n && a[r] > a[largest]) largest = r;
            if (largest == i) return;
            swap(a, i, largest);
            i = largest;
        }
    }

    private static void swap(int[] a, int i, int j) {
        int t = a[i];
        a[i] = a[j];
        a[j] = t;
    }
}
