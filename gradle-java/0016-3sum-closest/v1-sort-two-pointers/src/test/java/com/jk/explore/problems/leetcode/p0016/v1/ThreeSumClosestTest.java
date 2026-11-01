package com.jk.explore.problems.leetcode.p0016.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ThreeSumClosestTest {

    private final ThreeSumClosest solution = new ThreeSumClosest();

    @Test
    void examples() {
        assertEquals(2, solution.threeSumClosest(new int[]{-1, 2, 1, -4}, 1));
        assertEquals(0, solution.threeSumClosest(new int[]{0, 0, 0}, 1));
        assertEquals(3, solution.threeSumClosest(new int[]{1, 1, 1, 0}, 100));
    }
}
