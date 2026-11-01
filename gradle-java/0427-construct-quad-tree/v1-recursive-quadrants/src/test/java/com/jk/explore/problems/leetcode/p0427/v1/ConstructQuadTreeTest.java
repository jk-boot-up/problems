package com.jk.explore.problems.leetcode.p0427.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class ConstructQuadTreeTest {

    private final ConstructQuadTree solution = new ConstructQuadTree();

    /** Serializes like LeetCode: [isLeaf, val] per node in level order. */
    private static List<String> serialize(ConstructQuadTree.Node root) {
        List<String> out = new ArrayList<>();
        Deque<ConstructQuadTree.Node> q = new ArrayDeque<>(List.of(root));
        while (!q.isEmpty()) {
            ConstructQuadTree.Node n = q.poll();
            out.add(n.isLeaf ? "[1," + (n.val ? 1 : 0) + "]" : "[0,*]");
            if (!n.isLeaf) q.addAll(List.of(n.topLeft, n.topRight, n.bottomLeft, n.bottomRight));
        }
        return out;
    }

    @Test
    void checkerboard() {
        assertEquals(List.of("[0,*]", "[1,0]", "[1,1]", "[1,1]", "[1,0]"), serialize(solution.construct(new int[][]{{0, 1}, {1, 0}})));
    }

    @Test
    void uniform() {
        assertEquals(List.of("[1,1]"), serialize(solution.construct(new int[][]{{1, 1}, {1, 1}})));
    }

    @Test
    void mixed() {
        int[][] g = {{1, 1, 0, 0}, {1, 1, 0, 0}, {1, 1, 1, 1}, {1, 1, 1, 1}};
        assertEquals(List.of("[0,*]", "[1,1]", "[1,0]", "[1,1]", "[1,1]"), serialize(solution.construct(g)));
    }
}
