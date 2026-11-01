package com.jk.explore.problems.leetcode.p1376.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class TimeToInformTest {

    private final TimeToInform solution = new TimeToInform();

    @Test
    void examples() {
        assertEquals(0, solution.numOfMinutes(1, 0, new int[]{-1}, new int[]{0}));
        assertEquals(1, solution.numOfMinutes(6, 2, new int[]{2, 2, -1, 2, 2, 2}, new int[]{0, 0, 1, 0, 0, 0}));
        assertEquals(21, solution.numOfMinutes(7, 6, new int[]{1, 2, 3, 4, 5, 6, -1}, new int[]{0, 6, 5, 4, 3, 2, 1}));
        assertEquals(3, solution.numOfMinutes(4, 0, new int[]{-1, 0, 0, 1}, new int[]{1, 2, 5, 0}));
    }

    @Test
    void longChain() {
        int n = 100_000;
        int[] manager = new int[n], inform = new int[n];
        for (int i = 0; i < n; i++) {
            manager[i] = i - 1;
            inform[i] = 1;
        }
        assertEquals(n - 1, solution.numOfMinutes(n, 0, manager, inform));
    }
}
