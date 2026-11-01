package com.jk.explore.problems.leetcode.p1295.v1;

import java.util.*;

public class EvenNumberOfDigits {

    public int findNumbers(int[] nums) {
        int count = 0;
        for (int x : nums) {
            int digits = 0;
            for (int v = x; v > 0; v /= 10) digits++;
            if (digits % 2 == 0) count++;
        }
        return count;
    }
}
