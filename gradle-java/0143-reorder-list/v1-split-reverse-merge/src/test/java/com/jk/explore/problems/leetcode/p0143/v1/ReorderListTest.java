package com.jk.explore.problems.leetcode.p0143.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReorderListTest {

    private final ReorderList solution = new ReorderList();

    private int[] reorder(int... v) {
        ListNode head = ListNode.of(v);
        solution.reorderList(head);
        return ListNode.toArray(head);
    }

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 4, 2, 3}, reorder(1, 2, 3, 4));
        assertArrayEquals(new int[]{1, 5, 2, 4, 3}, reorder(1, 2, 3, 4, 5));
        assertArrayEquals(new int[]{1}, reorder(1));
    }
}
