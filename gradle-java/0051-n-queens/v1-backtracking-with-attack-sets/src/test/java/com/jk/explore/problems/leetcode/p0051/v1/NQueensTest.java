package com.jk.explore.problems.leetcode.p0051.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NQueensTest {

    private final NQueens solution = new NQueens();

    @Test
    void four() {
        assertEquals(List.of(List.of(".Q..", "...Q", "Q...", "..Q."), List.of("..Q.", "Q...", "...Q", ".Q..")), solution.solveNQueens(4));
    }

    @Test
    void counts() {
        assertEquals(1, solution.solveNQueens(1).size());
        assertEquals(92, solution.solveNQueens(8).size());
    }
}
