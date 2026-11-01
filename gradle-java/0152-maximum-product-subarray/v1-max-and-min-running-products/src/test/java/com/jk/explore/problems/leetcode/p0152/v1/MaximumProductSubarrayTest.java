package com.jk.explore.problems.leetcode.p0152.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumProductSubarrayTest {

    private final MaximumProductSubarray solution = new MaximumProductSubarray();

    @Test
    void examples() {
        assertEquals(6, solution.maxProduct(new int[]{2, 3, -2, 4}));
        assertEquals(0, solution.maxProduct(new int[]{-2, 0, -1}));
        assertEquals(24, solution.maxProduct(new int[]{-2, 3, -4}));
    }

    @Test
    void single() {
        assertEquals(-3, solution.maxProduct(new int[]{-3}));
    }
}
