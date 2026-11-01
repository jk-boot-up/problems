package com.jk.explore.problems.leetcode.p1491.v1;

import java.util.*;

public class AverageSalary {

    public double average(int[] salary) {
        long sum = 0;
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for (int s : salary) {
            sum += s;
            min = Math.min(min, s);
            max = Math.max(max, s);
        }
        return (double) (sum - min - max) / (salary.length - 2);
    }
}
