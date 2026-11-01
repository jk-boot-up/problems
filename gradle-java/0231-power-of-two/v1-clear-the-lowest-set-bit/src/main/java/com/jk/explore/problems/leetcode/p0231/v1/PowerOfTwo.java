package com.jk.explore.problems.leetcode.p0231.v1;

import java.util.*;

public class PowerOfTwo {

    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
    }
}
