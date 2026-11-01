package com.jk.explore.problems.leetcode.p1337.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class KWeakestRowsTest {

    private final KWeakestRows solution = new KWeakestRows();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 0, 3}, solution.kWeakestRows(new int[][]{{1, 1, 0, 0, 0}, {1, 1, 1, 1, 0}, {1, 0, 0, 0, 0}, {1, 1, 0, 0, 0}, {1, 1, 1, 1, 1}}, 3));
        assertArrayEquals(new int[]{0, 2}, solution.kWeakestRows(new int[][]{{1, 0, 0, 0}, {1, 1, 1, 1}, {1, 0, 0, 0}, {1, 0, 0, 0}}, 2));
        assertArrayEquals(new int[]{1, 0}, solution.kWeakestRows(new int[][]{{1, 1}, {0, 0}}, 2));
    }
}
