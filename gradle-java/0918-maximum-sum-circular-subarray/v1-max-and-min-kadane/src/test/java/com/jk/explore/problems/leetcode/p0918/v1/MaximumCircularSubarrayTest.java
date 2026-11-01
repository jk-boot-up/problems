package com.jk.explore.problems.leetcode.p0918.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumCircularSubarrayTest {

    private final MaximumCircularSubarray solution = new MaximumCircularSubarray();

    @ParameterizedTest
    @CsvSource(value = {"1,-2,3,-2:3", "5,-3,5:10", "-3,-2,-3:-2", "3,-1,2,-1:4", "-2:-2"}, delimiter = ':')
    void finds(String nums, int expected) {
        int[] a = Arrays.stream(nums.split(",")).mapToInt(Integer::parseInt).toArray();
        assertEquals(expected, solution.maxSubarraySumCircular(a));
    }
}
