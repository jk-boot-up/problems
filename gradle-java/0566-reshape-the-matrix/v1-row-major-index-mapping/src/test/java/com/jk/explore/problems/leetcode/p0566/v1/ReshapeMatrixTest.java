package com.jk.explore.problems.leetcode.p0566.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReshapeMatrixTest {

    private final ReshapeMatrix solution = new ReshapeMatrix();

    @Test
    void examples() {
        assertArrayEquals(new int[][]{{1, 2, 3, 4}}, solution.matrixReshape(new int[][]{{1, 2}, {3, 4}}, 1, 4));
        assertArrayEquals(new int[][]{{1, 2}, {3, 4}}, solution.matrixReshape(new int[][]{{1, 2}, {3, 4}}, 2, 4));
        assertArrayEquals(new int[][]{{1}, {2}, {3}, {4}}, solution.matrixReshape(new int[][]{{1, 2}, {3, 4}}, 4, 1));
    }
}
