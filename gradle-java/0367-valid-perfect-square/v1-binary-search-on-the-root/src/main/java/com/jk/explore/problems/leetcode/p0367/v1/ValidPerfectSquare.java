package com.jk.explore.problems.leetcode.p0367.v1;

import java.util.*;

public class ValidPerfectSquare {

    public boolean isPerfectSquare(int num) {
        long lo = 1, hi = Math.min(num, 46340);
        while (lo <= hi) {
            long mid = (lo + hi) >>> 1, sq = mid * mid;
            if (sq == num) return true;
            if (sq < num) lo = mid + 1;
            else hi = mid - 1;
        }
        return false;
    }
}
