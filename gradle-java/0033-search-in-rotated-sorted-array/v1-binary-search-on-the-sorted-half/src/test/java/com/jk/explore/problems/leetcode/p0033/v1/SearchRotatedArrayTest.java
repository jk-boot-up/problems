package com.jk.explore.problems.leetcode.p0033.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SearchRotatedArrayTest {

    private final SearchRotatedArray solution = new SearchRotatedArray();

    @ParameterizedTest
    @CsvSource({"0,4", "3,-1", "4,0", "2,6", "7,3"})
    void searches(int target, int expected) {
        assertEquals(expected, solution.search(new int[]{4, 5, 6, 7, 0, 1, 2}, target));
    }

    @Test
    void single() {
        assertEquals(-1, solution.search(new int[]{1}, 0));
        assertEquals(0, solution.search(new int[]{1}, 1));
    }
}
