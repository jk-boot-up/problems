package com.jk.explore.problems.leetcode.p1091.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ShortestPathBinaryMatrixTest {

    private final ShortestPathBinaryMatrix solution = new ShortestPathBinaryMatrix();

    @Test
    void examples() {
        assertEquals(2, solution.shortestPathBinaryMatrix(new int[][]{{0, 1}, {1, 0}}));
        assertEquals(4, solution.shortestPathBinaryMatrix(new int[][]{{0, 0, 0}, {1, 1, 0}, {1, 1, 0}}));
        assertEquals(-1, solution.shortestPathBinaryMatrix(new int[][]{{1, 0, 0}, {1, 1, 0}, {1, 1, 0}}));
        assertEquals(1, solution.shortestPathBinaryMatrix(new int[][]{{0}}));
        assertEquals(-1, solution.shortestPathBinaryMatrix(new int[][]{{0, 1}, {1, 1}}));
    }
}
