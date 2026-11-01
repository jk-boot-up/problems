package com.jk.explore.problems.leetcode.p0684.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RedundantConnectionTest {

    private final RedundantConnection solution = new RedundantConnection();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 3}, solution.findRedundantConnection(new int[][]{{1, 2}, {1, 3}, {2, 3}}));
        assertArrayEquals(new int[]{1, 4}, solution.findRedundantConnection(new int[][]{{1, 2}, {2, 3}, {3, 4}, {1, 4}, {1, 5}}));
    }
}
