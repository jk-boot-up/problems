package com.jk.explore.problems.leetcode.p0218.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SkylineTest {

    private final Skyline solution = new Skyline();

    @Test
    void examples() {
        assertEquals(List.of(List.of(2, 10), List.of(3, 15), List.of(7, 12), List.of(12, 0), List.of(15, 10), List.of(20, 8), List.of(24, 0)),
                solution.getSkyline(new int[][]{{2, 9, 10}, {3, 7, 15}, {5, 12, 12}, {15, 20, 10}, {19, 24, 8}}));
        assertEquals(List.of(List.of(0, 3), List.of(5, 0)), solution.getSkyline(new int[][]{{0, 2, 3}, {2, 5, 3}}));
    }

    @Test
    void nested() {
        assertEquals(List.of(List.of(1, 5), List.of(10, 0)), solution.getSkyline(new int[][]{{1, 10, 5}, {2, 3, 4}}));
        assertEquals(List.of(List.of(1, 3), List.of(2, 0)), solution.getSkyline(new int[][]{{1, 2, 1}, {1, 2, 2}, {1, 2, 3}}));
    }
}
