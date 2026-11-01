package com.jk.explore.problems.leetcode.p0074.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class Search2DMatrixTest {

    private final Search2DMatrix solution = new Search2DMatrix();
    private final int[][] matrix = {{1, 3, 5, 7}, {10, 11, 16, 20}, {23, 30, 34, 60}};

    @ParameterizedTest
    @CsvSource({"3,true", "13,false", "1,true", "60,true", "0,false", "61,false"})
    void searches(int target, boolean expected) {
        assertEquals(expected, solution.searchMatrix(matrix, target));
    }
}
