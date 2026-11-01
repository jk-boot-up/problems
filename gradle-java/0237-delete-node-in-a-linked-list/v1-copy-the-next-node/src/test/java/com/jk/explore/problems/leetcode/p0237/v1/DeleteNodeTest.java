package com.jk.explore.problems.leetcode.p0237.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DeleteNodeTest {

    private final DeleteNode solution = new DeleteNode();

    @Test
    void examples() {
        ListNode head = ListNode.of(4, 5, 1, 9);
        solution.deleteNode(head.next);
        assertArrayEquals(new int[]{4, 1, 9}, ListNode.toArray(head));
        ListNode other = ListNode.of(4, 5, 1, 9);
        solution.deleteNode(other.next.next);
        assertArrayEquals(new int[]{4, 5, 9}, ListNode.toArray(other));
        ListNode pair = ListNode.of(1, 2);
        solution.deleteNode(pair);
        assertArrayEquals(new int[]{2}, ListNode.toArray(pair));
    }
}
