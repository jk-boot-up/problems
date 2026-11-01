package com.jk.explore.problems.leetcode.p0264.v2;

import java.util.*;

public class UglyNumberII {

    public int nthUglyNumber(int n) {
        int[] ugly = new int[n];
        ugly[0] = 1;
        int i2 = 0, i3 = 0, i5 = 0;
        for (int k = 1; k < n; k++) {
            int a = ugly[i2] * 2, b = ugly[i3] * 3, c = ugly[i5] * 5;
            int next = Math.min(a, Math.min(b, c));
            ugly[k] = next;
            if (next == a) i2++;
            if (next == b) i3++;
            if (next == c) i5++;
        }
        return ugly[n - 1];
    }
}
