package com.jk.explore.problems.leetcode.p1791.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindCenterOfStarTest {

    private final FindCenterOfStar solution = new FindCenterOfStar();

    @Test
    void examples() {
        assertEquals(2, solution.findCenter(new int[][]{{1, 2}, {2, 3}, {4, 2}}));
        assertEquals(1, solution.findCenter(new int[][]{{1, 2}, {5, 1}, {1, 3}, {1, 4}}));
        assertEquals(3, solution.findCenter(new int[][]{{1, 3}, {3, 2}}));
    }
}
