package com.jk.explore.problems.leetcode.p0117.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PopulatingNextRightTest {

    private final PopulatingNextRight solution = new PopulatingNextRight();

    private static List<String> levels(PopulatingNextRight.Node root) {
        List<String> out = new ArrayList<>();
        for (PopulatingNextRight.Node start = root; start != null; ) {
            StringBuilder sb = new StringBuilder();
            PopulatingNextRight.Node nextStart = null;
            for (PopulatingNextRight.Node n = start; n != null; n = n.next) {
                sb.append(n.val).append(' ');
                if (nextStart == null) nextStart = n.left != null ? n.left : n.right;
            }
            out.add(sb.toString().trim());
            PopulatingNextRight.Node probe = start;
            while (nextStart == null && probe != null) {
                nextStart = probe.left != null ? probe.left : probe.right;
                probe = probe.next;
            }
            start = nextStart;
        }
        return out;
    }

    @Test
    void example() {
        var n4 = new PopulatingNextRight.Node(4);
        var n5 = new PopulatingNextRight.Node(5);
        var n7 = new PopulatingNextRight.Node(7);
        var root = new PopulatingNextRight.Node(1, new PopulatingNextRight.Node(2, n4, n5), new PopulatingNextRight.Node(3, null, n7));
        solution.connect(root);
        assertEquals(List.of("1", "2 3", "4 5 7"), levels(root));
        assertNull(n7.next);
    }

    @Test
    void empty() {
        assertNull(solution.connect(null));
    }
}
