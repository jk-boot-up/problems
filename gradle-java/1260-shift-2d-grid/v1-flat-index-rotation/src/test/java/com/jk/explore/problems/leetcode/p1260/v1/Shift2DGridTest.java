package com.jk.explore.problems.leetcode.p1260.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class Shift2DGridTest {

    private final Shift2DGrid solution = new Shift2DGrid();

    @Test
    void examples() {
        assertEquals(List.of(List.of(9, 1, 2), List.of(3, 4, 5), List.of(6, 7, 8)), solution.shiftGrid(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 1));
        assertEquals(List.of(List.of(1, 2, 3), List.of(4, 5, 6), List.of(7, 8, 9)), solution.shiftGrid(new int[][]{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, 9));
    }
}
