package com.jk.explore.problems.leetcode.p0149.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaxPointsOnALineTest {

    private final MaxPointsOnALine solution = new MaxPointsOnALine();

    @Test
    void diagonal() {
        assertEquals(3, solution.maxPoints(new int[][]{{1, 1}, {2, 2}, {3, 3}}));
    }

    @Test
    void mixed() {
        assertEquals(4, solution.maxPoints(new int[][]{{1, 1}, {3, 2}, {5, 3}, {4, 1}, {2, 3}, {1, 4}}));
    }

    @Test
    void verticalAndSingle() {
        assertEquals(3, solution.maxPoints(new int[][]{{0, 0}, {0, 5}, {0, -3}, {1, 1}}));
        assertEquals(1, solution.maxPoints(new int[][]{{7, 7}}));
    }
}
