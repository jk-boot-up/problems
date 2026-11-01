package com.jk.explore.problems.leetcode.p1523.v1;

import java.util.*;

public class CountOddsInRange {

    public int countOdds(int low, int high) {
        return (high + 1) / 2 - low / 2;
    }
}
