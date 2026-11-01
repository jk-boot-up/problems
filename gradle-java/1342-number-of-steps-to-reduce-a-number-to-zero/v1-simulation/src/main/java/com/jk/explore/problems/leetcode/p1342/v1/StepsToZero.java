package com.jk.explore.problems.leetcode.p1342.v1;

import java.util.*;

public class StepsToZero {

    public int numberOfSteps(int num) {
        int steps = 0;
        while (num > 0) {
            num = num % 2 == 0 ? num / 2 : num - 1;
            steps++;
        }
        return steps;
    }
}
