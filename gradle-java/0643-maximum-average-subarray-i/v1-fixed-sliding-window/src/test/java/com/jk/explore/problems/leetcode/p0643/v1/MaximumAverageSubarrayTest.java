package com.jk.explore.problems.leetcode.p0643.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumAverageSubarrayTest {

    private final MaximumAverageSubarray solution = new MaximumAverageSubarray();

    @Test
    void examples() {
        assertEquals(12.75, solution.findMaxAverage(new int[]{1, 12, -5, -6, 50, 3}, 4), 1e-9);
        assertEquals(5.0, solution.findMaxAverage(new int[]{5}, 1), 1e-9);
    }
}
