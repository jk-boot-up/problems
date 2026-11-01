package com.jk.explore.problems.leetcode.p1283.v1;

import java.util.*;

public class SmallestDivisor {

    public int smallestDivisor(int[] nums, int threshold) {
        int lo = 1, hi = 1;
        for (int v : nums) hi = Math.max(hi, v);
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            long sum = 0;
            for (int v : nums) sum += (v + mid - 1) / mid;
            if (sum <= threshold) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
