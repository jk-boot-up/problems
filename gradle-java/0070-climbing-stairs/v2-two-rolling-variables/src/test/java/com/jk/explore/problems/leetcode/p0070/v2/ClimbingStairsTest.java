package com.jk.explore.problems.leetcode.p0070.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ClimbingStairsTest {

    private final ClimbingStairs solution = new ClimbingStairs();

    @ParameterizedTest
    @CsvSource({"1,1", "2,2", "3,3", "5,8", "45,1836311903"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.climbStairs(n));
    }
}
