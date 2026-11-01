package com.jk.explore.problems.leetcode.p0876.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MiddleOfLinkedListTest {

    private final MiddleOfLinkedList solution = new MiddleOfLinkedList();

    @Test
    void examples() {
        assertArrayEquals(new int[]{3, 4, 5}, ListNode.toArray(solution.middleNode(ListNode.of(1, 2, 3, 4, 5))));
        assertArrayEquals(new int[]{4, 5, 6}, ListNode.toArray(solution.middleNode(ListNode.of(1, 2, 3, 4, 5, 6))));
    }
}
