package com.jk.explore.problems.leetcode.p1020.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumberOfEnclavesTest {

    private final NumberOfEnclaves solution = new NumberOfEnclaves();

    @Test
    void examples() {
        assertEquals(3, solution.numEnclaves(new int[][]{{0, 0, 0, 0}, {1, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}));
        assertEquals(0, solution.numEnclaves(new int[][]{{0, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}}));
        assertEquals(0, solution.numEnclaves(new int[][]{{1}}));
        assertEquals(1, solution.numEnclaves(new int[][]{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}));
    }
}
