package com.jk.explore.problems.leetcode.p0274.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class HIndexTest {

    private final HIndex solution = new HIndex();

    @Test
    void example1() {
        assertEquals(3, solution.hIndex(new int[]{3, 0, 6, 1, 5}));
    }

    @Test
    void example2() {
        assertEquals(1, solution.hIndex(new int[]{1, 3, 1}));
    }

    @Test
    void noCitations() {
        assertEquals(0, solution.hIndex(new int[]{0, 0}));
    }

    @Test
    void allHighlyCited() {
        assertEquals(3, solution.hIndex(new int[]{100, 100, 100}));
    }
}
