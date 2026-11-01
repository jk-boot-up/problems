package com.jk.explore.problems.leetcode.p1466.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReorderRoutesTest {

    private final ReorderRoutes solution = new ReorderRoutes();

    @Test
    void examples() {
        assertEquals(3, solution.minReorder(6, new int[][]{{0, 1}, {1, 3}, {2, 3}, {4, 0}, {4, 5}}));
        assertEquals(2, solution.minReorder(5, new int[][]{{1, 0}, {1, 2}, {3, 2}, {3, 4}}));
        assertEquals(0, solution.minReorder(3, new int[][]{{1, 0}, {2, 0}}));
    }
}
