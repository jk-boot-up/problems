package com.jk.explore.problems.leetcode.p0026.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveDuplicatesTest {

    private final RemoveDuplicates solution = new RemoveDuplicates();

    @Test
    void example1() {
        int[] nums = {1, 1, 2};
        int k = solution.removeDuplicates(nums);
        assertArrayEquals(new int[]{1, 2}, Arrays.copyOf(nums, k));
    }

    @Test
    void example2() {
        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int k = solution.removeDuplicates(nums);
        assertArrayEquals(new int[]{0, 1, 2, 3, 4}, Arrays.copyOf(nums, k));
    }

    @Test
    void singleElement() {
        assertEquals(1, solution.removeDuplicates(new int[]{5}));
    }

    @Test
    void allSame() {
        int[] nums = {2, 2, 2, 2};
        assertEquals(1, solution.removeDuplicates(nums));
    }
}
