package com.jk.explore.problems.leetcode.p0350.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IntersectionOfTwoArraysIITest {

    private final IntersectionOfTwoArraysII solution = new IntersectionOfTwoArraysII();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 2}, solution.intersect(new int[]{1, 2, 2, 1}, new int[]{2, 2}));
        int[] r = solution.intersect(new int[]{4, 9, 5}, new int[]{9, 4, 9, 8, 4});
        Arrays.sort(r);
        assertArrayEquals(new int[]{4, 9}, r);
    }
}
