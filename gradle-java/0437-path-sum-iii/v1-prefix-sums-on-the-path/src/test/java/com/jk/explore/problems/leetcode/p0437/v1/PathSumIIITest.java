package com.jk.explore.problems.leetcode.p0437.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PathSumIIITest {

    @Test
    void examples() {
        assertEquals(3, new PathSumIII().pathSum(TreeNode.of(10, 5, -3, 3, 2, null, 11, 3, -2, null, 1), 8));
        assertEquals(3, new PathSumIII().pathSum(TreeNode.of(5, 4, 8, 11, null, 13, 4, 7, 2, null, null, 5, 1), 22));
    }

    @Test
    void largeValues() {
        assertEquals(0, new PathSumIII().pathSum(TreeNode.of(1000000000, 1000000000, null, 294967296, null, 1000000000, null, 1000000000, null, 1000000000), 0));
    }
}
