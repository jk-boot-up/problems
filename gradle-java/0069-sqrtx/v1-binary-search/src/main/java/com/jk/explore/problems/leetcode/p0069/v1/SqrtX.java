package com.jk.explore.problems.leetcode.p0069.v1;

import java.util.*;

public class SqrtX {

    public int mySqrt(int x) {
        long lo = 0, hi = x;
        while (lo < hi) {
            long mid = (lo + hi + 1) / 2;
            if (mid * mid <= x) lo = mid; else hi = mid - 1;
        }
        return (int) lo;
    }
}
