package com.jk.explore.problems.leetcode.p0909.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SnakesAndLaddersTest {

    private final SnakesAndLadders solution = new SnakesAndLadders();

    @Test
    void example() {
        int[][] board = {
            {-1, -1, -1, -1, -1, -1}, {-1, -1, -1, -1, -1, -1}, {-1, -1, -1, -1, -1, -1},
            {-1, 35, -1, -1, 13, -1}, {-1, -1, -1, -1, -1, -1}, {-1, 15, -1, -1, -1, -1}};
        assertEquals(4, solution.snakesAndLadders(board));
    }

    @Test
    void small() {
        assertEquals(1, solution.snakesAndLadders(new int[][]{{-1, -1}, {-1, 3}}));
    }

    @Test
    void plainBoard() {
        assertEquals(2, solution.snakesAndLadders(new int[][]{{-1, -1, -1}, {-1, -1, -1}, {-1, -1, -1}}));
    }
}
