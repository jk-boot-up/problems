package com.jk.explore.problems.leetcode.p0029.v1;

import java.util.*;

public class DivideTwoIntegers {

    public int divide(int dividend, int divisor) {
        if (dividend == Integer.MIN_VALUE && divisor == -1) return Integer.MAX_VALUE;
        boolean negative = (dividend < 0) != (divisor < 0);
        int a = dividend > 0 ? -dividend : dividend, b = divisor > 0 ? -divisor : divisor; // both <= 0
        int quotient = 0;
        while (a <= b) {
            int chunk = b, multiple = 1;
            while (chunk >= (Integer.MIN_VALUE >> 1) && a <= chunk + chunk) {
                chunk += chunk;
                multiple += multiple;
            }
            a -= chunk;
            quotient += multiple;
        }
        return negative ? -quotient : quotient;
    }
}
