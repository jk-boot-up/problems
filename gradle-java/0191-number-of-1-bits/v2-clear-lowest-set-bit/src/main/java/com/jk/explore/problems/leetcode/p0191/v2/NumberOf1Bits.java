package com.jk.explore.problems.leetcode.p0191.v2;

import java.util.*;

public class NumberOf1Bits {

    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n &= n - 1;
            count++;
        }
        return count;
    }
}
