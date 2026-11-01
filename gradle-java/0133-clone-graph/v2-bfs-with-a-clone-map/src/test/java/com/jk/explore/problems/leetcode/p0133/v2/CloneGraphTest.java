package com.jk.explore.problems.leetcode.p0133.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CloneGraphTest {

    private final CloneGraph solution = new CloneGraph();

    private static CloneGraph.Node build(int[][] adj) {
        if (adj.length == 0) return null;
        CloneGraph.Node[] nodes = new CloneGraph.Node[adj.length];
        for (int i = 0; i < adj.length; i++) nodes[i] = new CloneGraph.Node(i + 1);
        for (int i = 0; i < adj.length; i++) for (int j : adj[i]) nodes[i].neighbors.add(nodes[j - 1]);
        return nodes[0];
    }

    /** Collects nodes by value and checks the clone shares no node with the original. */
    private static Map<Integer, CloneGraph.Node> nodes(CloneGraph.Node start) {
        Map<Integer, CloneGraph.Node> seen = new TreeMap<>();
        Deque<CloneGraph.Node> stack = new ArrayDeque<>(List.of(start));
        while (!stack.isEmpty()) {
            CloneGraph.Node n = stack.pop();
            if (seen.putIfAbsent(n.val, n) == null) stack.addAll(n.neighbors);
        }
        return seen;
    }

    @Test
    void square() {
        int[][] adj = {{2, 4}, {1, 3}, {2, 4}, {1, 3}};
        CloneGraph.Node original = build(adj), copy = solution.cloneGraph(original);
        Map<Integer, CloneGraph.Node> a = nodes(original), b = nodes(copy);
        assertEquals(a.keySet(), b.keySet());
        for (int v : a.keySet()) {
            assertNotSame(a.get(v), b.get(v));
            assertEquals(a.get(v).neighbors.stream().map(x -> x.val).toList(), b.get(v).neighbors.stream().map(x -> x.val).toList());
            for (CloneGraph.Node nb : b.get(v).neighbors) assertSame(b.get(nb.val), nb);
        }
    }

    @Test
    void singleNodeAndEmpty() {
        assertEquals(1, solution.cloneGraph(new CloneGraph.Node(1)).val);
        assertNull(solution.cloneGraph(null));
    }
}
