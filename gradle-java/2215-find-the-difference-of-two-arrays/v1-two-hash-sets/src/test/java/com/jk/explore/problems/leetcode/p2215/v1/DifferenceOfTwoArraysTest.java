package com.jk.explore.problems.leetcode.p2215.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DifferenceOfTwoArraysTest {

    private final DifferenceOfTwoArrays solution = new DifferenceOfTwoArrays();

    @Test
    void examples() {
        List<List<Integer>> r = solution.findDifference(new int[]{1, 2, 3}, new int[]{2, 4, 6});
        assertEquals(Set.of(1, 3), new HashSet<>(r.get(0)));
        assertEquals(Set.of(4, 6), new HashSet<>(r.get(1)));
        List<List<Integer>> s = solution.findDifference(new int[]{1, 2, 3, 3}, new int[]{1, 1, 2, 2});
        assertEquals(List.of(3), s.get(0));
        assertEquals(List.of(), s.get(1));
    }
}
