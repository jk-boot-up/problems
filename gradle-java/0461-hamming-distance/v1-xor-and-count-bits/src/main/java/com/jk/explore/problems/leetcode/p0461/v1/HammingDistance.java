package com.jk.explore.problems.leetcode.p0461.v1;

import java.util.*;

public class HammingDistance {

    public int hammingDistance(int x, int y) {
        int z = x ^ y, count = 0;
        while (z != 0) {
            z &= z - 1;
            count++;
        }
        return count;
    }
}
