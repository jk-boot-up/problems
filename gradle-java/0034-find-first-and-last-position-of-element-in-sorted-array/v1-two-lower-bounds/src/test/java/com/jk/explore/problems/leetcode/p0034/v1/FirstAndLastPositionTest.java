package com.jk.explore.problems.leetcode.p0034.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FirstAndLastPositionTest {

    private final FirstAndLastPosition solution = new FirstAndLastPosition();

    @Test
    void present() {
        assertArrayEquals(new int[]{3, 4}, solution.searchRange(new int[]{5, 7, 7, 8, 8, 10}, 8));
    }

    @Test
    void absent() {
        assertArrayEquals(new int[]{-1, -1}, solution.searchRange(new int[]{5, 7, 7, 8, 8, 10}, 6));
        assertArrayEquals(new int[]{-1, -1}, solution.searchRange(new int[]{}, 0));
    }

    @Test
    void maxValue() {
        assertArrayEquals(new int[]{0, 1}, solution.searchRange(new int[]{2147483647, 2147483647}, 2147483647));
    }
}
