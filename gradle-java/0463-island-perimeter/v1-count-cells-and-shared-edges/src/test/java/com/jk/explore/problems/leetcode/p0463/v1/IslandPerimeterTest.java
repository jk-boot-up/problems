package com.jk.explore.problems.leetcode.p0463.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IslandPerimeterTest {

    private final IslandPerimeter solution = new IslandPerimeter();

    @Test
    void examples() {
        assertEquals(16, solution.islandPerimeter(new int[][]{{0, 1, 0, 0}, {1, 1, 1, 0}, {0, 1, 0, 0}, {1, 1, 0, 0}}));
        assertEquals(4, solution.islandPerimeter(new int[][]{{1}}));
        assertEquals(4, solution.islandPerimeter(new int[][]{{1, 0}}));
        assertEquals(8, solution.islandPerimeter(new int[][]{{1, 1}, {1, 1}}));
    }
}
