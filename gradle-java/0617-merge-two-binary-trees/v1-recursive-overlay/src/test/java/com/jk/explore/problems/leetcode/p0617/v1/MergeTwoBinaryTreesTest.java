package com.jk.explore.problems.leetcode.p0617.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MergeTwoBinaryTreesTest {

    private final MergeTwoBinaryTrees solution = new MergeTwoBinaryTrees();

    @Test
    void examples() {
        assertEquals(Arrays.asList(3, 4, 5, 5, 4, null, 7), TreeNode.toList(solution.mergeTrees(TreeNode.of(1, 3, 2, 5), TreeNode.of(2, 1, 3, null, 4, null, 7))));
        assertEquals(List.of(2, 2), TreeNode.toList(solution.mergeTrees(TreeNode.of(1), TreeNode.of(1, 2))));
    }
}
