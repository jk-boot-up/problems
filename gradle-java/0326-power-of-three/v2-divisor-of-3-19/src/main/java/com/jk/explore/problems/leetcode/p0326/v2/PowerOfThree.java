package com.jk.explore.problems.leetcode.p0326.v2;

import java.util.*;

public class PowerOfThree {

    public boolean isPowerOfThree(int n) {
        return n > 0 && 1162261467 % n == 0;
    }
}
