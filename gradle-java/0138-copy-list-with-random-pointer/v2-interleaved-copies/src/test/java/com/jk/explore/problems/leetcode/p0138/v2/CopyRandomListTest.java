package com.jk.explore.problems.leetcode.p0138.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CopyRandomListTest {

    private final CopyRandomList solution = new CopyRandomList();

    /** Builds a list from [val, randomIndex] pairs (randomIndex -1 = null). */
    private static CopyRandomList.Node build(int[][] spec) {
        CopyRandomList.Node[] nodes = new CopyRandomList.Node[spec.length];
        for (int i = 0; i < spec.length; i++) nodes[i] = new CopyRandomList.Node(spec[i][0]);
        for (int i = 0; i < spec.length; i++) {
            if (i + 1 < spec.length) nodes[i].next = nodes[i + 1];
            if (spec[i][1] >= 0) nodes[i].random = nodes[spec[i][1]];
        }
        return spec.length == 0 ? null : nodes[0];
    }

    private static List<String> describe(CopyRandomList.Node head) {
        List<CopyRandomList.Node> order = new ArrayList<>();
        for (CopyRandomList.Node n = head; n != null; n = n.next) order.add(n);
        List<String> out = new ArrayList<>();
        for (CopyRandomList.Node n : order) out.add(n.val + ":" + (n.random == null ? -1 : order.indexOf(n.random)));
        return out;
    }

    @Test
    void deepCopy() {
        int[][] spec = {{7, -1}, {13, 0}, {11, 4}, {10, 2}, {1, 0}};
        CopyRandomList.Node original = build(spec);
        CopyRandomList.Node copy = solution.copyRandomList(original);
        assertEquals(describe(build(spec)), describe(copy));
        assertEquals(describe(build(spec)), describe(original), "original must be restored");
        for (CopyRandomList.Node a = original, b = copy; a != null; a = a.next, b = b.next) assertNotSame(a, b);
    }

    @Test
    void empty() {
        assertNull(solution.copyRandomList(null));
    }
}
