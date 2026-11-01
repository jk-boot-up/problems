package com.jk.explore.problems.leetcode.p0080.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveDuplicatesIITest {

    private final RemoveDuplicatesII solution = new RemoveDuplicatesII();

    @Test
    void example1() {
        int[] nums = {1, 1, 1, 2, 2, 3};
        int k = solution.removeDuplicates(nums);
        assertArrayEquals(new int[]{1, 1, 2, 2, 3}, Arrays.copyOf(nums, k));
    }

    @Test
    void example2() {
        int[] nums = {0, 0, 1, 1, 1, 1, 2, 3, 3};
        int k = solution.removeDuplicates(nums);
        assertArrayEquals(new int[]{0, 0, 1, 1, 2, 3, 3}, Arrays.copyOf(nums, k));
    }

    @Test
    void shortArrays() {
        assertEquals(1, solution.removeDuplicates(new int[]{1}));
        assertEquals(2, solution.removeDuplicates(new int[]{1, 1}));
    }
}
