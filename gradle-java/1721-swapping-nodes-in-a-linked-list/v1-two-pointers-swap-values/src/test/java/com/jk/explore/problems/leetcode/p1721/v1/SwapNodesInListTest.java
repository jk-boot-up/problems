package com.jk.explore.problems.leetcode.p1721.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SwapNodesInListTest {

    private final SwapNodesInList solution = new SwapNodesInList();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 4, 3, 2, 5}, ListNode.toArray(solution.swapNodes(ListNode.of(1, 2, 3, 4, 5), 2)));
        assertArrayEquals(new int[]{7, 9, 6, 6, 8, 7, 3, 0, 9, 5}, ListNode.toArray(solution.swapNodes(ListNode.of(7, 9, 6, 6, 7, 8, 3, 0, 9, 5), 5)));
        assertArrayEquals(new int[]{1}, ListNode.toArray(solution.swapNodes(ListNode.of(1), 1)));
        assertArrayEquals(new int[]{2, 1}, ListNode.toArray(solution.swapNodes(ListNode.of(1, 2), 1)));
        assertArrayEquals(new int[]{1, 2, 3}, ListNode.toArray(solution.swapNodes(ListNode.of(1, 2, 3), 2)));
    }
}
