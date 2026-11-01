package com.jk.explore.problems.leetcode.p0704.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BinarySearchTest {

    private final BinarySearch solution = new BinarySearch();

    @ParameterizedTest
    @CsvSource({"9,4", "2,-1", "-1,0", "12,5", "13,-1"})
    void searches(int target, int expected) {
        assertEquals(expected, solution.search(new int[]{-1, 0, 3, 5, 9, 12}, target));
    }
}
