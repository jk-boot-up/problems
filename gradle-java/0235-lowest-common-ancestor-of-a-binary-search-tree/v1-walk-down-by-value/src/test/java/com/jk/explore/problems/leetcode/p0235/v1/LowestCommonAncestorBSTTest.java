package com.jk.explore.problems.leetcode.p0235.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LowestCommonAncestorBSTTest {

    private final LowestCommonAncestorBST solution = new LowestCommonAncestorBST();
    private final TreeNode root = TreeNode.of(6, 2, 8, 0, 4, 7, 9, null, null, 3, 5);

    private TreeNode node(int v) {
        TreeNode n = root;
        while (n.val != v) n = v < n.val ? n.left : n.right;
        return n;
    }

    @Test
    void examples() {
        assertEquals(6, solution.lowestCommonAncestor(root, node(2), node(8)).val);
        assertEquals(2, solution.lowestCommonAncestor(root, node(2), node(4)).val);
        assertEquals(4, solution.lowestCommonAncestor(root, node(3), node(5)).val);
    }
}
