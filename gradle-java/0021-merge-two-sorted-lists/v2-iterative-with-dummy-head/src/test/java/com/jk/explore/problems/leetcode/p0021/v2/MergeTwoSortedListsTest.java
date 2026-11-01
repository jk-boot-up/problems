package com.jk.explore.problems.leetcode.p0021.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MergeTwoSortedListsTest {

    private final MergeTwoSortedLists solution = new MergeTwoSortedLists();

    @Test
    void interleaved() {
        assertArrayEquals(new int[]{1, 1, 2, 3, 4, 4}, ListNode.toArray(solution.mergeTwoLists(ListNode.of(1, 2, 4), ListNode.of(1, 3, 4))));
    }

    @Test
    void bothEmpty() {
        assertNull(solution.mergeTwoLists(null, null));
    }

    @Test
    void oneEmpty() {
        assertArrayEquals(new int[]{0}, ListNode.toArray(solution.mergeTwoLists(null, ListNode.of(0))));
    }
}
