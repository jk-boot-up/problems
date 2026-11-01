package com.jk.explore.problems.leetcode.p0141.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LinkedListCycleTest {

    private final LinkedListCycle solution = new LinkedListCycle();

    /** Builds a list whose tail points back to the node at index pos (pos = -1: no cycle). */
    private static ListNode withCycle(int pos, int... values) {
        ListNode[] nodes = new ListNode[values.length];
        for (int i = 0; i < values.length; i++) nodes[i] = new ListNode(values[i]);
        for (int i = 0; i + 1 < values.length; i++) nodes[i].next = nodes[i + 1];
        if (pos >= 0) nodes[values.length - 1].next = nodes[pos];
        return nodes[0];
    }

    @Test
    void cycle() {
        assertTrue(solution.hasCycle(withCycle(1, 3, 2, 0, -4)));
    }

    @Test
    void selfLoop() {
        assertTrue(solution.hasCycle(withCycle(0, 1)));
    }

    @Test
    void noCycle() {
        assertFalse(solution.hasCycle(ListNode.of(1, 2)));
        assertFalse(solution.hasCycle(null));
    }
}
