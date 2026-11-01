package com.jk.explore.problems.leetcode.p0209.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumSizeSubarraySumTest {

    private final MinimumSizeSubarraySum solution = new MinimumSizeSubarraySum();

    @Test
    void example1() {
        assertEquals(2, solution.minSubArrayLen(7, new int[]{2, 3, 1, 2, 4, 3}));
    }

    @Test
    void singleElementSuffices() {
        assertEquals(1, solution.minSubArrayLen(4, new int[]{1, 4, 4}));
    }

    @Test
    void impossible() {
        assertEquals(0, solution.minSubArrayLen(11, new int[]{1, 1, 1, 1, 1, 1, 1, 1}));
    }
}
