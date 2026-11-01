package com.jk.explore.problems.leetcode.p0024.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SwapNodesInPairsTest {

    private final SwapNodesInPairs solution = new SwapNodesInPairs();

    @Test
    void examples() {
        assertArrayEquals(new int[]{2, 1, 4, 3}, ListNode.toArray(solution.swapPairs(ListNode.of(1, 2, 3, 4))));
        assertArrayEquals(new int[]{2, 1, 3}, ListNode.toArray(solution.swapPairs(ListNode.of(1, 2, 3))));
        assertNull(solution.swapPairs(null));
    }
}
