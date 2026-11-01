package com.jk.explore.problems.leetcode.p0852.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PeakIndexInMountainTest {

    private final PeakIndexInMountain solution = new PeakIndexInMountain();

    @Test
    void examples() {
        assertEquals(1, solution.peakIndexInMountainArray(new int[]{0, 1, 0}));
        assertEquals(1, solution.peakIndexInMountainArray(new int[]{0, 2, 1, 0}));
        assertEquals(4, solution.peakIndexInMountainArray(new int[]{1, 3, 5, 7, 9, 4, 2}));
    }
}
