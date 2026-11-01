package com.jk.explore.problems.leetcode.p0334.v1;

import java.util.*;

public class IncreasingTriplet {

    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE, second = Integer.MAX_VALUE;
        for (int x : nums) {
            if (x <= first) first = x;
            else if (x <= second) second = x;
            else return true;
        }
        return false;
    }
}
