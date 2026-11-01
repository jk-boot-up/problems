package com.jk.explore.problems.leetcode.p2130.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MaximumTwinSumTest {

    private final MaximumTwinSum solution = new MaximumTwinSum();

    @Test
    void examples() {
        assertEquals(6, solution.pairSum(ListNode.of(5, 4, 2, 1)));
        assertEquals(7, solution.pairSum(ListNode.of(4, 2, 2, 3)));
        assertEquals(100001, solution.pairSum(ListNode.of(1, 100000)));
    }
}
