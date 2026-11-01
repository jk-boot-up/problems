package com.jk.explore.problems.leetcode.p1448.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CountGoodNodesTest {

    private final CountGoodNodes solution = new CountGoodNodes();

    @Test
    void examples() {
        assertEquals(4, solution.goodNodes(TreeNode.of(3, 1, 4, 3, null, 1, 5)));
        assertEquals(3, solution.goodNodes(TreeNode.of(3, 3, null, 4, 2)));
        assertEquals(1, solution.goodNodes(TreeNode.of(1)));
    }
}
