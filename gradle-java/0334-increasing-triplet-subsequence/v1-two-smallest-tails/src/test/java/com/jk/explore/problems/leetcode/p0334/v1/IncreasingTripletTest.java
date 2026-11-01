package com.jk.explore.problems.leetcode.p0334.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IncreasingTripletTest {

    private final IncreasingTriplet solution = new IncreasingTriplet();

    @Test
    void examples() {
        assertTrue(solution.increasingTriplet(new int[]{1, 2, 3, 4, 5}));
        assertFalse(solution.increasingTriplet(new int[]{5, 4, 3, 2, 1}));
        assertTrue(solution.increasingTriplet(new int[]{2, 1, 5, 0, 4, 6}));
    }
}
