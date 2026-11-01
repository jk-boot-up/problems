package com.jk.explore.problems.leetcode.p0200.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumberOfIslandsTest {

    private final NumberOfIslands solution = new NumberOfIslands();

    private static char[][] grid(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void oneIsland() {
        assertEquals(1, solution.numIslands(grid("11110", "11010", "11000", "00000")));
    }

    @Test
    void threeIslands() {
        assertEquals(3, solution.numIslands(grid("11000", "11000", "00100", "00011")));
    }

    @Test
    void noLand() {
        assertEquals(0, solution.numIslands(grid("000")));
    }
}
