package com.jk.explore.problems.leetcode.p0743.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NetworkDelayTimeTest {

    private final NetworkDelayTime solution = new NetworkDelayTime();

    @Test
    void examples() {
        assertEquals(2, solution.networkDelayTime(new int[][]{{2, 1, 1}, {2, 3, 1}, {3, 4, 1}}, 4, 2));
        assertEquals(1, solution.networkDelayTime(new int[][]{{1, 2, 1}}, 2, 1));
        assertEquals(-1, solution.networkDelayTime(new int[][]{{1, 2, 1}}, 2, 2));
    }

    @Test
    void shorterIndirectPath() {
        assertEquals(3, solution.networkDelayTime(new int[][]{{1, 2, 5}, {1, 3, 1}, {3, 2, 2}}, 3, 1));
    }
}
