package com.jk.explore.problems.leetcode.p0797.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AllPathsSourceTargetTest {

    private final AllPathsSourceTarget solution = new AllPathsSourceTarget();

    @Test
    void examples() {
        assertEquals(List.of(List.of(0, 1, 3), List.of(0, 2, 3)), solution.allPathsSourceTarget(new int[][]{{1, 2}, {3}, {3}, {}}));
        assertEquals(5, solution.allPathsSourceTarget(new int[][]{{4, 3, 1}, {3, 2, 4}, {3}, {4}, {}}).size());
    }
}
