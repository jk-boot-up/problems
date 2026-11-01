package com.jk.explore.problems.leetcode.p0086.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PartitionListTest {

    private final PartitionList solution = new PartitionList();

    @Test
    void example1() {
        assertArrayEquals(new int[]{1, 2, 2, 4, 3, 5}, ListNode.toArray(solution.partition(ListNode.of(1, 4, 3, 2, 5, 2), 3)));
    }

    @Test
    void twoNodes() {
        assertArrayEquals(new int[]{1, 2}, ListNode.toArray(solution.partition(ListNode.of(2, 1), 2)));
    }

    @Test
    void empty() {
        assertNull(solution.partition(null, 0));
    }
}
