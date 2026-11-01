package com.jk.explore.problems.leetcode.p0872.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LeafSimilarTreesTest {

    private final LeafSimilarTrees solution = new LeafSimilarTrees();

    @Test
    void examples() {
        assertTrue(solution.leafSimilar(TreeNode.of(3, 5, 1, 6, 2, 9, 8, null, null, 7, 4),
                TreeNode.of(3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8)));
        assertFalse(solution.leafSimilar(TreeNode.of(1, 2, 3), TreeNode.of(1, 3, 2)));
    }
}
