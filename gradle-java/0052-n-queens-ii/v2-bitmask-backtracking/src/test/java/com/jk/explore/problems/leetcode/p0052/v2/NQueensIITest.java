package com.jk.explore.problems.leetcode.p0052.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NQueensIITest {

    private final NQueensII solution = new NQueensII();

    @ParameterizedTest
    @CsvSource({"1,1", "2,0", "3,0", "4,2", "5,10", "8,92", "9,352"})
    void counts(int n, int expected) {
        assertEquals(expected, solution.totalNQueens(n));
    }
}
