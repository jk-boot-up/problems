package com.jk.explore.problems.leetcode.p0036.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ValidSudokuTest {

    private final ValidSudoku solution = new ValidSudoku();

    private static char[][] board(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    private static final String[] VALID = {
        "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
        "7...2...6", ".6....28.", "...419..5", "....8..79"};

    @Test
    void validBoard() {
        assertTrue(solution.isValidSudoku(board(VALID)));
    }

    @Test
    void duplicateInColumn() {
        String[] rows = VALID.clone();
        rows[0] = "83..7....";
        assertFalse(solution.isValidSudoku(board(rows)));
    }

    @Test
    void duplicateInBox() {
        String[] rows = VALID.clone();
        rows[1] = "6.5195...";
        assertFalse(solution.isValidSudoku(board(rows)));
    }
}
