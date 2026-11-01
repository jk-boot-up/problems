package com.jk.explore.problems.leetcode.p1732.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class HighestAltitudeTest {

    private final HighestAltitude solution = new HighestAltitude();

    @Test
    void examples() {
        assertEquals(1, solution.largestAltitude(new int[]{-5, 1, 5, 0, -7}));
        assertEquals(0, solution.largestAltitude(new int[]{-4, -3, -2, -1, 4, 3, 2}));
    }
}
