package com.jk.explore.problems.leetcode.p0108.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SortedArrayToBSTTest {

    private final SortedArrayToBST solution = new SortedArrayToBST();

    private static int height(TreeNode n) {
        if (n == null) return 0;
        int l = height(n.left), r = height(n.right);
        if (l < 0 || r < 0 || Math.abs(l - r) > 1) return -1;
        return 1 + Math.max(l, r);
    }

    private static void inorder(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorder(n.left, out);
        out.add(n.val);
        inorder(n.right, out);
    }

    @Test
    void balancedAndSorted() {
        int[] nums = {-10, -3, 0, 5, 9};
        TreeNode root = solution.sortedArrayToBST(nums);
        assertTrue(height(root) > 0);
        List<Integer> values = new ArrayList<>();
        inorder(root, values);
        assertEquals(List.of(-10, -3, 0, 5, 9), values);
    }

    @Test
    void large() {
        int[] nums = new int[1000];
        for (int i = 0; i < nums.length; i++) nums[i] = i;
        assertEquals(10, height(solution.sortedArrayToBST(nums)));
    }
}
