package com.jk.explore.problems.leetcode.p0329.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestIncreasingPathTest {

    private final LongestIncreasingPath solution = new LongestIncreasingPath();

    @Test
    void examples() {
        assertEquals(4, solution.longestIncreasingPath(new int[][]{{9, 9, 4}, {6, 6, 8}, {2, 1, 1}}));
        assertEquals(4, solution.longestIncreasingPath(new int[][]{{3, 4, 5}, {3, 2, 6}, {2, 2, 1}}));
        assertEquals(1, solution.longestIncreasingPath(new int[][]{{1}}));
    }
}
