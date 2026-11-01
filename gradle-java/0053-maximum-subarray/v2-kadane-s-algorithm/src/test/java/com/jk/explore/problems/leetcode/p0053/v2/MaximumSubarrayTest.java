package com.jk.explore.problems.leetcode.p0053.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumSubarrayTest {

    private final MaximumSubarray solution = new MaximumSubarray();

    @Test
    void classic() {
        assertEquals(6, solution.maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}));
    }

    @Test
    void allNegative() {
        assertEquals(-1, solution.maxSubArray(new int[]{-3, -1, -2}));
    }

    @Test
    void wholeArray() {
        assertEquals(23, solution.maxSubArray(new int[]{5, 4, -1, 7, 8}));
    }
}
