package com.jk.explore.problems.leetcode.p0054.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SpiralMatrixTest {

    private final SpiralMatrix solution = new SpiralMatrix();

    @Test
    void square() {
        assertEquals(List.of(1, 2, 3, 6, 9, 8, 7, 4, 5), solution.spiralOrder(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}));
    }

    @Test
    void wide() {
        assertEquals(List.of(1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7),
                solution.spiralOrder(new int[][]{{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}}));
    }

    @Test
    void singleColumn() {
        assertEquals(List.of(1, 2, 3), solution.spiralOrder(new int[][]{{1}, {2}, {3}}));
    }
}
