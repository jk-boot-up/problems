package com.jk.explore.problems.leetcode.p0109.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SortedListToBSTTest {

    private final SortedListToBST solution = new SortedListToBST();

    private static void inorder(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorder(n.left, out);
        out.add(n.val);
        inorder(n.right, out);
    }

    private static int height(TreeNode n) {
        return n == null ? 0 : 1 + Math.max(height(n.left), height(n.right));
    }

    @Test
    void balancedAndSorted() {
        TreeNode root = solution.sortedListToBST(ListNode.of(-10, -3, 0, 5, 9));
        List<Integer> values = new ArrayList<>();
        inorder(root, values);
        assertEquals(List.of(-10, -3, 0, 5, 9), values);
        assertEquals(3, height(root));
        assertNull(solution.sortedListToBST(null));
    }
}
