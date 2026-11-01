package com.jk.explore.problems.leetcode.p0228.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SummaryRangesTest {

    private final SummaryRanges solution = new SummaryRanges();

    @Test
    void example1() {
        assertEquals(List.of("0->2", "4->5", "7"), solution.summaryRanges(new int[]{0, 1, 2, 4, 5, 7}));
    }

    @Test
    void example2() {
        assertEquals(List.of("0", "2->4", "6", "8->9"), solution.summaryRanges(new int[]{0, 2, 3, 4, 6, 8, 9}));
    }

    @Test
    void empty() {
        assertEquals(List.of(), solution.summaryRanges(new int[]{}));
    }
}
