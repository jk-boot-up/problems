package com.jk.explore.problems.leetcode.p1588.v1;

import java.util.*;

public class SumOddLengthSubarrays {

    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length, sum = 0;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + arr[i];
        for (int i = 0; i < n; i++)
            for (int len = 1; i + len <= n; len += 2) sum += prefix[i + len] - prefix[i];
        return sum;
    }
}
