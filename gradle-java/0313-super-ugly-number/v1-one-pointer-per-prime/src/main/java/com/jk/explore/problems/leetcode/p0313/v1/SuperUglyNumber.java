package com.jk.explore.problems.leetcode.p0313.v1;

import java.util.*;

public class SuperUglyNumber {

    public int nthSuperUglyNumber(int n, int[] primes) {
        long[] ugly = new long[n];
        ugly[0] = 1;
        int[] idx = new int[primes.length];
        for (int i = 1; i < n; i++) {
            long next = Long.MAX_VALUE;
            for (int j = 0; j < primes.length; j++) next = Math.min(next, ugly[idx[j]] * primes[j]);
            ugly[i] = next;
            for (int j = 0; j < primes.length; j++) if (ugly[idx[j]] * primes[j] == next) idx[j]++;
        }
        return (int) ugly[n - 1];
    }
}
