package com.jk.explore.problems.leetcode.p0059.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SpiralMatrixIITest {

    private final SpiralMatrixII solution = new SpiralMatrixII();

    @Test
    void examples() {
        assertArrayEquals(new int[][]{{1, 2, 3}, {8, 9, 4}, {7, 6, 5}}, solution.generateMatrix(3));
        assertArrayEquals(new int[][]{{1}}, solution.generateMatrix(1));
        assertArrayEquals(new int[][]{{1, 2, 3, 4}, {12, 13, 14, 5}, {11, 16, 15, 6}, {10, 9, 8, 7}}, solution.generateMatrix(4));
    }
}
