package com.jk.explore.problems.leetcode.p0204.v1;

import java.util.*;

public class CountPrimes {

    public int countPrimes(int n) {
        int count = 0;
        for (int x = 2; x < n; x++) if (isPrime(x)) count++;
        return count;
    }

    private boolean isPrime(int x) {
        for (int d = 2; (long) d * d <= x; d++) if (x % d == 0) return false;
        return true;
    }
}
