package com.jk.explore.problems.leetcode.p0875.v1;

import java.util.*;

public class KokoEatingBananas {

    public int minEatingSpeed(int[] piles, int h) {
        int lo = 1, hi = Arrays.stream(piles).max().getAsInt();
        while (lo < hi) {
            int k = (lo + hi) >>> 1;
            long hours = 0;
            for (int p : piles) hours += (p - 1) / k + 1; // ceil(p / k) without overflow
            if (hours <= h) hi = k; else lo = k + 1;
        }
        return lo;
    }
}
