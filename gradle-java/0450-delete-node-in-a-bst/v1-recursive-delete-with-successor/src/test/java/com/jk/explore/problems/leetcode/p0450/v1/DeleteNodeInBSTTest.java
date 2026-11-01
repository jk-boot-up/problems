package com.jk.explore.problems.leetcode.p0450.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DeleteNodeInBSTTest {

    private final DeleteNodeInBST solution = new DeleteNodeInBST();

    private static void inorder(TreeNode n, List<Integer> out) {
        if (n == null) return;
        inorder(n.left, out);
        out.add(n.val);
        inorder(n.right, out);
    }

    private List<Integer> afterDelete(int key, Integer... tree) {
        List<Integer> out = new ArrayList<>();
        inorder(solution.deleteNode(TreeNode.of(tree), key), out);
        return out;
    }

    @Test
    void twoChildren() {
        assertEquals(List.of(2, 4, 5, 6, 7), afterDelete(3, 5, 3, 6, 2, 4, null, 7));
    }

    @Test
    void leafRootAndMissing() {
        assertEquals(List.of(2, 3, 4, 5, 6), afterDelete(7, 5, 3, 6, 2, 4, null, 7));
        assertEquals(List.of(2, 3, 4, 6, 7), afterDelete(5, 5, 3, 6, 2, 4, null, 7));
        assertEquals(List.of(2, 3, 4, 5, 6, 7), afterDelete(0, 5, 3, 6, 2, 4, null, 7));
    }
}
