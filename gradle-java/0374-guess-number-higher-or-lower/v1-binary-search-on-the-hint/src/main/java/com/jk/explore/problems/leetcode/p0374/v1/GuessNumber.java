package com.jk.explore.problems.leetcode.p0374.v1;

import java.util.*;

public class GuessNumber {

    private final int pick;

    public GuessNumber(int pick) {
        this.pick = pick;
    }

    /** The game's API: -1 if num is too high, 1 if too low, 0 if correct. */
    int guess(int num) {
        return Integer.compare(pick, num);
    }

    public int guessNumber(int n) {
        int lo = 1, hi = n;
        while (true) {
            int mid = (lo + hi) >>> 1;
            int r = guess(mid);
            if (r == 0) return mid;
            if (r < 0) hi = mid - 1; else lo = mid + 1;
        }
    }
}
