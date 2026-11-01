package com.jk.explore.problems.leetcode.p0204.v2;

import java.util.*;

public class CountPrimes {

    public int countPrimes(int n) {
        boolean[] composite = new boolean[Math.max(n, 2)];
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (composite[i]) continue;
            count++;
            for (long j = (long) i * i; j < n; j += i) composite[(int) j] = true;
        }
        return count;
    }
}
