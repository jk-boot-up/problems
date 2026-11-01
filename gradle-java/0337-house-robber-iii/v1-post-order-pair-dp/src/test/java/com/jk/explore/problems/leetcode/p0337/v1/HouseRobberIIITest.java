package com.jk.explore.problems.leetcode.p0337.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class HouseRobberIIITest {

    private final HouseRobberIII solution = new HouseRobberIII();

    @Test
    void examples() {
        assertEquals(7, solution.rob(TreeNode.of(3, 2, 3, null, 3, null, 1)));
        assertEquals(9, solution.rob(TreeNode.of(3, 4, 5, 1, 3, null, 1)));
    }
}
