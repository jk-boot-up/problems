package com.jk.explore.problems.leetcode.p0013.v1;

import java.util.*;

public class RomanToInteger {

    private static int value(char c) {
        return switch (c) {
            case 'I' -> 1;
            case 'V' -> 5;
            case 'X' -> 10;
            case 'L' -> 50;
            case 'C' -> 100;
            case 'D' -> 500;
            case 'M' -> 1000;
            default -> throw new IllegalArgumentException("Not a Roman symbol: " + c);
        };
    }

    public int romanToInt(String s) {
        int total = 0;
        for (int i = 0; i < s.length(); i++) {
            int v = value(s.charAt(i));
            if (i + 1 < s.length() && v < value(s.charAt(i + 1))) {
                total -= v;
            } else {
                total += v;
            }
        }
        return total;
    }
}
