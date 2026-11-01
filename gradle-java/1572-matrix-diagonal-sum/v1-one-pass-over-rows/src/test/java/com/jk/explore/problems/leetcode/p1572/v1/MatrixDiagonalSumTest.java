package com.jk.explore.problems.leetcode.p1572.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MatrixDiagonalSumTest {

    private final MatrixDiagonalSum solution = new MatrixDiagonalSum();

    @Test
    void examples() {
        assertEquals(25, solution.diagonalSum(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}));
        assertEquals(8, solution.diagonalSum(new int[][]{{1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}, {1, 1, 1, 1}}));
        assertEquals(5, solution.diagonalSum(new int[][]{{5}}));
    }
}
