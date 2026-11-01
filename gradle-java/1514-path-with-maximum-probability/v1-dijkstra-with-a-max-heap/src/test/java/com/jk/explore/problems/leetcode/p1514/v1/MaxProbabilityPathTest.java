package com.jk.explore.problems.leetcode.p1514.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaxProbabilityPathTest {

    private final MaxProbabilityPath solution = new MaxProbabilityPath();

    @Test
    void examples() {
        int[][] e = {{0, 1}, {1, 2}, {0, 2}};
        assertEquals(0.25, solution.maxProbability(3, e, new double[]{0.5, 0.5, 0.2}, 0, 2), 1e-9);
        assertEquals(0.3, solution.maxProbability(3, e, new double[]{0.5, 0.5, 0.3}, 0, 2), 1e-9);
        assertEquals(0.0, solution.maxProbability(3, new int[][]{{0, 1}}, new double[]{0.5}, 0, 2), 1e-9);
        assertEquals(0.72, solution.maxProbability(4, new int[][]{{0, 1}, {1, 3}, {0, 2}, {2, 3}}, new double[]{0.9, 0.8, 0.95, 0.7}, 0, 3), 1e-9);
    }
}
