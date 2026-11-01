package com.jk.explore.problems.leetcode.p0863.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DistanceKTest {

    private final DistanceK solution = new DistanceK();

    private TreeNode find(TreeNode n, int v) {
        if (n == null || n.val == v) return n;
        TreeNode l = find(n.left, v);
        return l != null ? l : find(n.right, v);
    }

    private List<Integer> run(TreeNode root, int target, int k) {
        List<Integer> out = new ArrayList<>(solution.distanceK(root, find(root, target), k));
        Collections.sort(out);
        return out;
    }

    @Test
    void examples() {
        TreeNode root = TreeNode.of(3, 5, 1, 6, 2, 0, 8, null, null, 7, 4);
        assertEquals(List.of(1, 4, 7), run(root, 5, 2));
        assertEquals(List.of(5), run(root, 5, 0));
        assertEquals(List.of(0, 2, 6, 8), run(root, 3, 2));
        assertEquals(List.of(), run(TreeNode.of(1), 1, 3));
        assertEquals(List.of(1), run(root, 7, 4));
    }
}
