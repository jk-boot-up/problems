package com.jk.explore.problems.leetcode.p0236.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LowestCommonAncestorTest {

    private final LowestCommonAncestor solution = new LowestCommonAncestor();

    private static TreeNode find(TreeNode n, int val) {
        if (n == null || n.val == val) return n;
        TreeNode l = find(n.left, val);
        return l != null ? l : find(n.right, val);
    }

    private final TreeNode root = TreeNode.of(3, 5, 1, 6, 2, 0, 8, null, null, 7, 4);

    @Test
    void differentSides() {
        assertEquals(3, solution.lowestCommonAncestor(root, find(root, 5), find(root, 1)).val);
    }

    @Test
    void ancestorOfItself() {
        assertEquals(5, solution.lowestCommonAncestor(root, find(root, 5), find(root, 4)).val);
    }

    @Test
    void deepPair() {
        assertEquals(2, solution.lowestCommonAncestor(root, find(root, 7), find(root, 4)).val);
    }
}
