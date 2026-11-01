package com.jk.explore.problems.leetcode.p0674.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestContinuousIncreasingTest {

    private final LongestContinuousIncreasing solution = new LongestContinuousIncreasing();

    @Test
    void examples() {
        assertEquals(3, solution.findLengthOfLCIS(new int[]{1, 3, 5, 4, 7}));
        assertEquals(1, solution.findLengthOfLCIS(new int[]{2, 2, 2, 2, 2}));
    }
}
