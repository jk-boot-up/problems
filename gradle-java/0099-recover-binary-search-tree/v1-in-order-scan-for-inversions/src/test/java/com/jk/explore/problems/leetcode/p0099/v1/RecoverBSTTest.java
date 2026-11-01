package com.jk.explore.problems.leetcode.p0099.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RecoverBSTTest {

    private final RecoverBST solution = new RecoverBST();

    @Test
    void examples() {
        TreeNode a = TreeNode.of(1, 3, null, null, 2);
        solution.recoverTree(a);
        assertEquals(Arrays.asList(3, 1, null, null, 2), TreeNode.toList(a));
        TreeNode b = TreeNode.of(3, 1, 4, null, null, 2);
        solution.recoverTree(b);
        assertEquals(Arrays.asList(2, 1, 4, null, null, 3), TreeNode.toList(b));
    }
}
