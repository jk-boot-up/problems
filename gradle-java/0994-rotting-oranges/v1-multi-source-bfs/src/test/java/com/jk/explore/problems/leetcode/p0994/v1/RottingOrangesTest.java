package com.jk.explore.problems.leetcode.p0994.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RottingOrangesTest {

    private final RottingOranges solution = new RottingOranges();

    @Test
    void examples() {
        assertEquals(4, solution.orangesRotting(new int[][]{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}));
        assertEquals(-1, solution.orangesRotting(new int[][]{{2, 1, 1}, {0, 1, 1}, {1, 0, 1}}));
        assertEquals(0, solution.orangesRotting(new int[][]{{0, 2}}));
    }
}
