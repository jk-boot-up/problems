package com.jk.explore.problems.leetcode.p0082.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RemoveDuplicatesListIITest {

    private final RemoveDuplicatesListII solution = new RemoveDuplicatesListII();

    @Test
    void middleRuns() {
        assertArrayEquals(new int[]{1, 2, 5}, ListNode.toArray(solution.deleteDuplicates(ListNode.of(1, 2, 3, 3, 4, 4, 5))));
    }

    @Test
    void runAtHead() {
        assertArrayEquals(new int[]{2, 3}, ListNode.toArray(solution.deleteDuplicates(ListNode.of(1, 1, 1, 2, 3))));
    }

    @Test
    void allDuplicates() {
        assertNull(solution.deleteDuplicates(ListNode.of(1, 1)));
    }
}
