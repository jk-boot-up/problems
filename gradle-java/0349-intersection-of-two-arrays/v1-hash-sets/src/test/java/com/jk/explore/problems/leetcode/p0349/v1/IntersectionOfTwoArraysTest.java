package com.jk.explore.problems.leetcode.p0349.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IntersectionOfTwoArraysTest {

    private final IntersectionOfTwoArrays solution = new IntersectionOfTwoArrays();

    private static Set<Integer> set(int[] a) {
        Set<Integer> s = new HashSet<>();
        for (int x : a) s.add(x);
        return s;
    }

    @Test
    void examples() {
        assertArrayEquals(new int[]{2}, solution.intersection(new int[]{1, 2, 2, 1}, new int[]{2, 2}));
        assertEquals(Set.of(4, 9), set(solution.intersection(new int[]{4, 9, 5}, new int[]{9, 4, 9, 8, 4})));
    }
}
