package com.jk.explore.problems.leetcode.p0206.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ReverseLinkedListTest {

    private final ReverseLinkedList solution = new ReverseLinkedList();

    @Test
    void five() {
        assertArrayEquals(new int[]{5, 4, 3, 2, 1}, ListNode.toArray(solution.reverseList(ListNode.of(1, 2, 3, 4, 5))));
    }

    @Test
    void emptyAndSingle() {
        assertNull(solution.reverseList(null));
        assertArrayEquals(new int[]{1}, ListNode.toArray(solution.reverseList(ListNode.of(1))));
    }
}
