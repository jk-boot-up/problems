package com.jk.explore.problems.leetcode.p0258.v1;

import java.util.*;

public class AddDigits {

    public int addDigits(int num) {
        while (num >= 10) {
            int sum = 0;
            for (int n = num; n > 0; n /= 10) sum += n % 10;
            num = sum;
        }
        return num;
    }
}
