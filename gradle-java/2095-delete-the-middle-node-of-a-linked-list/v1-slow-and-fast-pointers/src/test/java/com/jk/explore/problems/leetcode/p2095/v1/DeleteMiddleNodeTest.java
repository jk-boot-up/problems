package com.jk.explore.problems.leetcode.p2095.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DeleteMiddleNodeTest {

    private final DeleteMiddleNode solution = new DeleteMiddleNode();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 3, 4, 1, 2, 6}, ListNode.toArray(solution.deleteMiddle(ListNode.of(1, 3, 4, 7, 1, 2, 6))));
        assertArrayEquals(new int[]{1, 2, 4}, ListNode.toArray(solution.deleteMiddle(ListNode.of(1, 2, 3, 4))));
        assertArrayEquals(new int[]{2}, ListNode.toArray(solution.deleteMiddle(ListNode.of(2, 1))));
        assertNull(solution.deleteMiddle(ListNode.of(1)));
    }
}
