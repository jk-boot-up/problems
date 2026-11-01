package com.jk.explore.problems.leetcode.p0658.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindKClosestElementsTest {

    private final FindKClosestElements solution = new FindKClosestElements();

    @Test
    void examples() {
        assertEquals(List.of(1, 2, 3, 4), solution.findClosestElements(new int[]{1, 2, 3, 4, 5}, 4, 3));
        assertEquals(List.of(1, 1, 2, 3), solution.findClosestElements(new int[]{1, 1, 2, 3, 4, 5}, 4, -1));
        assertEquals(List.of(3, 4), solution.findClosestElements(new int[]{1, 3, 4, 8}, 2, 5));
    }
}
