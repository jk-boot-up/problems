package com.jk.explore.problems.leetcode.p1162.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class AsFarFromLandTest {

    private final AsFarFromLand solution = new AsFarFromLand();

    @Test
    void examples() {
        assertEquals(2, solution.maxDistance(new int[][]{{1, 0, 1}, {0, 0, 0}, {1, 0, 1}}));
        assertEquals(4, solution.maxDistance(new int[][]{{1, 0, 0}, {0, 0, 0}, {0, 0, 0}}));
        assertEquals(-1, solution.maxDistance(new int[][]{{1, 1}, {1, 1}}));
        assertEquals(-1, solution.maxDistance(new int[][]{{0, 0}, {0, 0}}));
    }
}
