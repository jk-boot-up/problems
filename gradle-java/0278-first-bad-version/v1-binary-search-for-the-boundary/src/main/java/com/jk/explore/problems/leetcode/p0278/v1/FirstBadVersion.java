package com.jk.explore.problems.leetcode.p0278.v1;

import java.util.*;

public class FirstBadVersion {

    private final java.util.function.IntPredicate isBadVersion;

    public FirstBadVersion(java.util.function.IntPredicate isBadVersion) {
        this.isBadVersion = isBadVersion;
    }

    public int firstBadVersion(int n) {
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (isBadVersion.test(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
