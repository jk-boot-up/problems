package com.jk.explore.problems.leetcode.p0342.v1;

import java.util.*;

public class PowerOfFour {

    public boolean isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0x55555555) != 0;
    }
}
