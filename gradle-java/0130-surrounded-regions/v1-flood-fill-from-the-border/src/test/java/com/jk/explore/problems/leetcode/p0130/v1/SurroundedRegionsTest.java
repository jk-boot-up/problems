package com.jk.explore.problems.leetcode.p0130.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SurroundedRegionsTest {

    private final SurroundedRegions solution = new SurroundedRegions();

    private static char[][] board(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void example() {
        char[][] b = board("XXXX", "XOOX", "XXOX", "XOXX");
        solution.solve(b);
        assertArrayEquals(board("XXXX", "XXXX", "XXXX", "XOXX"), b);
    }

    @Test
    void borderConnected() {
        char[][] b = board("OOO", "OXO", "OOO");
        solution.solve(b);
        assertArrayEquals(board("OOO", "OXO", "OOO"), b);
    }

    @Test
    void single() {
        char[][] b = board("X");
        solution.solve(b);
        assertArrayEquals(board("X"), b);
    }
}
