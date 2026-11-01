package com.jk.explore.problems.leetcode.p0088.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MergeSortedArrayTest {

    private final MergeSortedArray solution = new MergeSortedArray();

    @Test
    void mergesInterleavedValues() {
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        solution.merge(nums1, 3, new int[]{2, 5, 6}, 3);
        assertArrayEquals(new int[]{1, 2, 2, 3, 5, 6}, nums1);
    }

    @Test
    void emptySecondArray() {
        int[] nums1 = {1};
        solution.merge(nums1, 1, new int[]{}, 0);
        assertArrayEquals(new int[]{1}, nums1);
    }

    @Test
    void emptyFirstArray() {
        int[] nums1 = {0};
        solution.merge(nums1, 0, new int[]{1}, 1);
        assertArrayEquals(new int[]{1}, nums1);
    }

    @Test
    void allOfSecondAreSmaller() {
        int[] nums1 = {4, 5, 6, 0, 0, 0};
        solution.merge(nums1, 3, new int[]{1, 2, 3}, 3);
        assertArrayEquals(new int[]{1, 2, 3, 4, 5, 6}, nums1);
    }
}
