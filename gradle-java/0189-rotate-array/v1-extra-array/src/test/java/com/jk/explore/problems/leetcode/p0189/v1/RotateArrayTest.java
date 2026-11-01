package com.jk.explore.problems.leetcode.p0189.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RotateArrayTest {

    private final RotateArray solution = new RotateArray();

    @Test
    void example1() {
        int[] nums = {1, 2, 3, 4, 5, 6, 7};
        solution.rotate(nums, 3);
        assertArrayEquals(new int[]{5, 6, 7, 1, 2, 3, 4}, nums);
    }

    @Test
    void example2() {
        int[] nums = {-1, -100, 3, 99};
        solution.rotate(nums, 2);
        assertArrayEquals(new int[]{3, 99, -1, -100}, nums);
    }

    @Test
    void kLargerThanLength() {
        int[] nums = {1, 2};
        solution.rotate(nums, 3);
        assertArrayEquals(new int[]{2, 1}, nums);
    }

    @Test
    void kZero() {
        int[] nums = {1, 2, 3};
        solution.rotate(nums, 0);
        assertArrayEquals(new int[]{1, 2, 3}, nums);
    }
}
