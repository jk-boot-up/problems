package com.jk.explore.problems.leetcode.p0092.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseLinkedListIITest {

    private final ReverseLinkedListII solution = new ReverseLinkedListII();

    @Test
    void middle() {
        assertArrayEquals(new int[]{1, 4, 3, 2, 5}, ListNode.toArray(solution.reverseBetween(ListNode.of(1, 2, 3, 4, 5), 2, 4)));
    }

    @Test
    void single() {
        assertArrayEquals(new int[]{5}, ListNode.toArray(solution.reverseBetween(ListNode.of(5), 1, 1)));
    }

    @Test
    void whole() {
        assertArrayEquals(new int[]{3, 2, 1}, ListNode.toArray(solution.reverseBetween(ListNode.of(1, 2, 3), 1, 3)));
    }
}
