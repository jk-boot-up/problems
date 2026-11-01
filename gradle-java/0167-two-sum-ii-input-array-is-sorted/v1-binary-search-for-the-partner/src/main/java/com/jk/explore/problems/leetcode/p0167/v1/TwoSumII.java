package com.jk.explore.problems.leetcode.p0167.v1;

import java.util.*;

public class TwoSumII {

    public int[] twoSum(int[] numbers, int target) {
        for (int i = 0; i < numbers.length; i++) {
            int want = target - numbers[i], lo = i + 1, hi = numbers.length - 1;
            while (lo <= hi) {
                int mid = (lo + hi) >>> 1;
                if (numbers[mid] == want) return new int[]{i + 1, mid + 1};
                if (numbers[mid] < want) lo = mid + 1; else hi = mid - 1;
            }
        }
        throw new IllegalArgumentException("No solution");
    }
}
