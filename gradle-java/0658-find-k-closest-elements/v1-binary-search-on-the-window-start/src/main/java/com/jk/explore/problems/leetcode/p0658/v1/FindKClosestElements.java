package com.jk.explore.problems.leetcode.p0658.v1;

import java.util.*;

public class FindKClosestElements {

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int lo = 0, hi = arr.length - k;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (x - arr[mid] > arr[mid + k] - x) lo = mid + 1; else hi = mid;
        }
        List<Integer> out = new ArrayList<>();
        for (int i = lo; i < lo + k; i++) out.add(arr[i]);
        return out;
    }
}
