package com.jk.explore.problems.leetcode.p0077.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CombinationsTest {

    private final Combinations solution = new Combinations();

    @Test
    void fourChooseTwo() {
        assertEquals(List.of(List.of(1, 2), List.of(1, 3), List.of(1, 4), List.of(2, 3), List.of(2, 4), List.of(3, 4)), solution.combine(4, 2));
    }

    @Test
    void chooseAll() {
        assertEquals(List.of(List.of(1, 2, 3)), solution.combine(3, 3));
    }

    @Test
    void count() {
        assertEquals(184756, solution.combine(20, 10).size());
    }
}
