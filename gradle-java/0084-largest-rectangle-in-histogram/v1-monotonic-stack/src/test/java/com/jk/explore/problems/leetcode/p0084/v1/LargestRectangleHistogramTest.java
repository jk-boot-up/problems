package com.jk.explore.problems.leetcode.p0084.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LargestRectangleHistogramTest {

    private final LargestRectangleHistogram solution = new LargestRectangleHistogram();

    @Test
    void examples() {
        assertEquals(10, solution.largestRectangleArea(new int[]{2, 1, 5, 6, 2, 3}));
        assertEquals(4, solution.largestRectangleArea(new int[]{2, 4}));
    }

    @Test
    void flat() {
        assertEquals(9, solution.largestRectangleArea(new int[]{3, 3, 3}));
    }
}
