package com.jk.explore.problems.leetcode.p0538.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class BSTToGreaterTreeTest {

    private final BSTToGreaterTree solution = new BSTToGreaterTree();

    @Test
    void examples() {
        assertEquals(Arrays.asList(30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null, null, 8),
                TreeNode.toList(solution.convertBST(TreeNode.of(4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8))));
        assertEquals(Arrays.asList(1, null, 1), TreeNode.toList(solution.convertBST(TreeNode.of(0, null, 1))));
        assertNull(solution.convertBST(null));
    }
}
