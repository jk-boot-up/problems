package com.jk.explore.problems.leetcode.p0240.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class Search2DMatrixIITest {

    private final Search2DMatrixII solution = new Search2DMatrixII();
    private final int[][] m = {{1, 4, 7, 11, 15}, {2, 5, 8, 12, 19}, {3, 6, 9, 16, 22}, {10, 13, 14, 17, 24}, {18, 21, 23, 26, 30}};

    @ParameterizedTest
    @CsvSource({"5,true", "20,false", "30,true", "1,true", "0,false"})
    void searches(int target, boolean expected) {
        assertEquals(expected, solution.searchMatrix(m, target));
    }
}
