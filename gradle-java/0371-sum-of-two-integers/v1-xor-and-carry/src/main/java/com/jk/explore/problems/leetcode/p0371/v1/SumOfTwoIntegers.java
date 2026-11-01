package com.jk.explore.problems.leetcode.p0371.v1;

import java.util.*;

public class SumOfTwoIntegers {

    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = (a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
}
