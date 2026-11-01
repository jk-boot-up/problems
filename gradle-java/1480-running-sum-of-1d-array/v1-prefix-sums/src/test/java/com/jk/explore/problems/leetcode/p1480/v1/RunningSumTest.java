package com.jk.explore.problems.leetcode.p1480.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RunningSumTest {

    private final RunningSum solution = new RunningSum();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 3, 6, 10}, solution.runningSum(new int[]{1, 2, 3, 4}));
        assertArrayEquals(new int[]{3, 4, 6, 16, 17}, solution.runningSum(new int[]{3, 1, 2, 10, 1}));
    }
}
