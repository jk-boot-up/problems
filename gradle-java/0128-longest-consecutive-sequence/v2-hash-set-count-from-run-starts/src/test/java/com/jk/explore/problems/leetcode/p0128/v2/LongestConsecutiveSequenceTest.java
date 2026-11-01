package com.jk.explore.problems.leetcode.p0128.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LongestConsecutiveSequenceTest {

    private final LongestConsecutiveSequence solution = new LongestConsecutiveSequence();

    @Test
    void example1() {
        assertEquals(4, solution.longestConsecutive(new int[]{100, 4, 200, 1, 3, 2}));
    }

    @Test
    void withDuplicates() {
        assertEquals(9, solution.longestConsecutive(new int[]{0, 3, 7, 2, 5, 8, 4, 6, 0, 1}));
    }

    @Test
    void empty() {
        assertEquals(0, solution.longestConsecutive(new int[]{}));
    }
}
