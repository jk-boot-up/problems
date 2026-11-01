package com.jk.explore.problems.leetcode.p0494.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TargetSumTest {

    private final TargetSum solution = new TargetSum();

    @Test
    void examples() {
        assertEquals(5, solution.findTargetSumWays(new int[]{1, 1, 1, 1, 1}, 3));
        assertEquals(1, solution.findTargetSumWays(new int[]{1}, 1));
    }

    @Test
    void zeros() {
        assertEquals(4, solution.findTargetSumWays(new int[]{0, 0, 1}, 1));
        assertEquals(0, solution.findTargetSumWays(new int[]{1}, 2));
    }
}
