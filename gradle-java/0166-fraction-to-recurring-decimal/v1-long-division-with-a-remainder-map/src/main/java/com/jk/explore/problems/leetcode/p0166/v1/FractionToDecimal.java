package com.jk.explore.problems.leetcode.p0166.v1;

import java.util.*;

public class FractionToDecimal {

    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        StringBuilder sb = new StringBuilder();
        if ((numerator < 0) ^ (denominator < 0)) sb.append('-');
        long n = Math.abs((long) numerator), d = Math.abs((long) denominator);
        sb.append(n / d);
        long r = n % d;
        if (r == 0) return sb.toString();
        sb.append('.');
        MyHashMap<Long, Integer> seenAt = new MyHashMap<>();
        while (r != 0) {
            Integer at = seenAt.get(r);
            if (at != null) {
                sb.insert((int) at, '(');
                sb.append(')');
                break;
            }
            seenAt.put(r, sb.length());
            r *= 10;
            sb.append(r / d);
            r %= d;
        }
        return sb.toString();
    }
}
