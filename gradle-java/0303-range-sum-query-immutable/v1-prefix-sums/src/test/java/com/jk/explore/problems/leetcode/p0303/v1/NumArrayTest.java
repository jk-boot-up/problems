package com.jk.explore.problems.leetcode.p0303.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumArrayTest {

    @Test
    void example() {
        NumArray a = new NumArray(new int[]{-2, 0, 3, -5, 2, -1});
        assertEquals(1, a.sumRange(0, 2));
        assertEquals(-1, a.sumRange(2, 5));
        assertEquals(-3, a.sumRange(0, 5));
        assertEquals(3, a.sumRange(2, 2));
    }
}
