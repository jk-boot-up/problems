package com.jk.explore.problems.leetcode.p0201.v1;

import java.util.*;

public class RangeBitwiseAnd {

    public int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        while (left != right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        return left << shift;
    }
}
