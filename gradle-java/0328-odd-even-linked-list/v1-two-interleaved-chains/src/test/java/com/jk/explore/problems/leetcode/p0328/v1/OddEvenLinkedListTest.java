package com.jk.explore.problems.leetcode.p0328.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class OddEvenLinkedListTest {

    private final OddEvenLinkedList solution = new OddEvenLinkedList();

    @Test
    void examples() {
        assertArrayEquals(new int[]{1, 3, 5, 2, 4}, ListNode.toArray(solution.oddEvenList(ListNode.of(1, 2, 3, 4, 5))));
        assertArrayEquals(new int[]{2, 3, 6, 7, 1, 5, 4}, ListNode.toArray(solution.oddEvenList(ListNode.of(2, 1, 3, 5, 6, 4, 7))));
        assertNull(solution.oddEvenList(null));
    }
}
