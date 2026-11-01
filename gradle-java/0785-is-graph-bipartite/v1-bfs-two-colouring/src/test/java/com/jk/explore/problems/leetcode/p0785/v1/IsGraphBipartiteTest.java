package com.jk.explore.problems.leetcode.p0785.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IsGraphBipartiteTest {

    private final IsGraphBipartite solution = new IsGraphBipartite();

    @Test
    void examples() {
        assertFalse(solution.isBipartite(new int[][]{{1, 2, 3}, {0, 2}, {0, 1, 3}, {0, 2}}));
        assertTrue(solution.isBipartite(new int[][]{{1, 3}, {0, 2}, {1, 3}, {0, 2}}));
        assertTrue(solution.isBipartite(new int[][]{{}, {2}, {1}}));
    }
}
