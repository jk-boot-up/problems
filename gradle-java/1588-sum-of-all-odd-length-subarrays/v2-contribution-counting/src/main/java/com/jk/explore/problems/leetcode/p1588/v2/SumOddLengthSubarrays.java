package com.jk.explore.problems.leetcode.p1588.v2;

import java.util.*;

public class SumOddLengthSubarrays {

    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length, sum = 0;
        for (int i = 0; i < n; i++) sum += arr[i] * (((i + 1) * (n - i) + 1) / 2);
        return sum;
    }
}
