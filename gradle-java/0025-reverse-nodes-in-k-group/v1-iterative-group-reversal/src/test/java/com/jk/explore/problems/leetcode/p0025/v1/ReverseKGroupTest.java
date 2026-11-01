package com.jk.explore.problems.leetcode.p0025.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseKGroupTest {

    private final ReverseKGroup solution = new ReverseKGroup();

    @Test
    void pairs() {
        assertArrayEquals(new int[]{2, 1, 4, 3, 5}, ListNode.toArray(solution.reverseKGroup(ListNode.of(1, 2, 3, 4, 5), 2)));
    }

    @Test
    void triples() {
        assertArrayEquals(new int[]{3, 2, 1, 4, 5}, ListNode.toArray(solution.reverseKGroup(ListNode.of(1, 2, 3, 4, 5), 3)));
    }

    @Test
    void kOne() {
        assertArrayEquals(new int[]{1, 2}, ListNode.toArray(solution.reverseKGroup(ListNode.of(1, 2), 1)));
    }
}
