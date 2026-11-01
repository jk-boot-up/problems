package com.jk.explore.problems.leetcode.p0019.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveNthFromEndTest {

    private final RemoveNthFromEnd solution = new RemoveNthFromEnd();

    @Test
    void middle() {
        assertArrayEquals(new int[]{1, 2, 3, 5}, ListNode.toArray(solution.removeNthFromEnd(ListNode.of(1, 2, 3, 4, 5), 2)));
    }

    @Test
    void onlyNode() {
        assertNull(solution.removeNthFromEnd(ListNode.of(1), 1));
    }

    @Test
    void head() {
        assertArrayEquals(new int[]{2}, ListNode.toArray(solution.removeNthFromEnd(ListNode.of(1, 2), 2)));
    }
}
