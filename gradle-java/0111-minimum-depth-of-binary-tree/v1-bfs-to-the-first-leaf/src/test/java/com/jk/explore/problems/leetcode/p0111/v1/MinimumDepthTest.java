package com.jk.explore.problems.leetcode.p0111.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MinimumDepthTest {

    private final MinimumDepth solution = new MinimumDepth();

    @Test
    void examples() {
        assertEquals(2, solution.minDepth(TreeNode.of(3, 9, 20, null, null, 15, 7)));
        assertEquals(5, solution.minDepth(TreeNode.of(2, null, 3, null, 4, null, 5, null, 6)));
        assertEquals(0, solution.minDepth(null));
    }
}
