package com.jk.explore.problems.leetcode.p0142.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LinkedListCycleIITest {

    private final LinkedListCycleII solution = new LinkedListCycleII();

    private static ListNode[] build(int pos, int... values) {
        ListNode[] nodes = new ListNode[values.length];
        for (int i = 0; i < values.length; i++) nodes[i] = new ListNode(values[i]);
        for (int i = 0; i + 1 < values.length; i++) nodes[i].next = nodes[i + 1];
        if (pos >= 0) nodes[values.length - 1].next = nodes[pos];
        return nodes;
    }

    @Test
    void cycle() {
        ListNode[] n = build(1, 3, 2, 0, -4);
        assertSame(n[1], solution.detectCycle(n[0]));
        ListNode[] m = build(0, 1, 2);
        assertSame(m[0], solution.detectCycle(m[0]));
    }

    @Test
    void noCycle() {
        assertNull(solution.detectCycle(build(-1, 1, 2, 3)[0]));
    }
}
