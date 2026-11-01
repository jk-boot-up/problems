package com.jk.explore.problems.leetcode.p0037.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SudokuSolverTest {

    @Test
    void classic() {
        String[] in = {"53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"};
        String[] out = {"534678912", "672195348", "198342567", "859761423", "426853791", "713924856", "961537284", "287419635", "345286179"};
        char[][] board = Arrays.stream(in).map(String::toCharArray).toArray(char[][]::new);
        new SudokuSolver().solveSudoku(board);
        for (int i = 0; i < 9; i++) assertEquals(out[i], new String(board[i]));
    }
}
