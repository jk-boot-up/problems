package com.jk.explore.problems.leetcode.p0023.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MergeKSortedListsTest {

    private final MergeKSortedLists solution = new MergeKSortedLists();

    @Test
    void three() {
        ListNode[] lists = {ListNode.of(1, 4, 5), ListNode.of(1, 3, 4), ListNode.of(2, 6)};
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4, 5, 6}, ListNode.toArray(solution.mergeKLists(lists)));
    }

    @Test
    void empty() {
        assertNull(solution.mergeKLists(new ListNode[]{}));
        assertNull(solution.mergeKLists(new ListNode[]{null}));
    }

    @Test
    void many() {
        ListNode[] lists = new ListNode[7];
        for (int i = 0; i < 7; i++) lists[i] = ListNode.of(i, i + 7, i + 14);
        int[] expected = new int[21];
        for (int i = 0; i < 21; i++) expected[i] = i;
        assertArrayEquals(expected, ListNode.toArray(solution.mergeKLists(lists)));
    }
}
