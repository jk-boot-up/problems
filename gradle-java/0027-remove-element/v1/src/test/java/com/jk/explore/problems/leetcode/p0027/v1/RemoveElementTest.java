package com.jk.explore.problems.leetcode.p0027.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveElementTest {

    private final RemoveElement solution = new RemoveElement();

    private static void assertPrefix(int[] expected, int[] nums, int k) {
        assertEquals(expected.length, k);
        int[] head = Arrays.copyOf(nums, k);
        Arrays.sort(head);
        int[] exp = expected.clone();
        Arrays.sort(exp);
        assertArrayEquals(exp, head);
    }

    @Test
    void example1() {
        int[] nums = {3, 2, 2, 3};
        assertPrefix(new int[]{2, 2}, nums, solution.removeElement(nums, 3));
    }

    @Test
    void example2() {
        int[] nums = {0, 1, 2, 2, 3, 0, 4, 2};
        assertPrefix(new int[]{0, 1, 3, 0, 4}, nums, solution.removeElement(nums, 2));
    }

    @Test
    void emptyArray() {
        assertEquals(0, solution.removeElement(new int[]{}, 1));
    }

    @Test
    void allRemoved() {
        int[] nums = {7, 7, 7};
        assertEquals(0, solution.removeElement(nums, 7));
    }
}
