package com.jk.explore.problems.leetcode.p1926.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NearestExitTest {

    private final NearestExit solution = new NearestExit();

    private static char[][] m(String... rows) {
        return Arrays.stream(rows).map(String::toCharArray).toArray(char[][]::new);
    }

    @Test
    void examples() {
        assertEquals(1, solution.nearestExit(m("++.+", "...+", "+++."), new int[]{1, 2}));
        assertEquals(2, solution.nearestExit(m("+++", "...", "+++"), new int[]{1, 0}));
        assertEquals(-1, solution.nearestExit(m(".+"), new int[]{0, 0}));
    }
}
