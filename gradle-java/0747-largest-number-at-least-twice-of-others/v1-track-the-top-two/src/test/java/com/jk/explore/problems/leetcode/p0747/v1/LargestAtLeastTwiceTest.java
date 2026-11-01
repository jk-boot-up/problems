package com.jk.explore.problems.leetcode.p0747.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LargestAtLeastTwiceTest {

    private final LargestAtLeastTwice solution = new LargestAtLeastTwice();

    @Test
    void examples() {
        assertEquals(1, solution.dominantIndex(new int[]{3, 6, 1, 0}));
        assertEquals(-1, solution.dominantIndex(new int[]{1, 2, 3, 4}));
        assertEquals(0, solution.dominantIndex(new int[]{1, 0}));
    }
}
