package com.jk.explore.problems.leetcode.p0011.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ContainerWithMostWaterTest {

    private final ContainerWithMostWater solution = new ContainerWithMostWater();

    @Test
    void example1() {
        assertEquals(49, solution.maxArea(new int[]{1, 8, 6, 2, 5, 4, 8, 3, 7}));
    }

    @Test
    void twoLines() {
        assertEquals(1, solution.maxArea(new int[]{1, 1}));
    }

    @Test
    void decreasing() {
        assertEquals(16, solution.maxArea(new int[]{4, 3, 2, 1, 4}));
    }
}
