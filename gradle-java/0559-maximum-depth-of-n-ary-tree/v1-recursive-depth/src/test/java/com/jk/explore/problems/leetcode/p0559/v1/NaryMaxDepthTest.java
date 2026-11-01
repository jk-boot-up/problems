package com.jk.explore.problems.leetcode.p0559.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NaryMaxDepthTest {

    private final NaryMaxDepth solution = new NaryMaxDepth();

    private static NaryMaxDepth.Node n(int v, NaryMaxDepth.Node... kids) {
        return new NaryMaxDepth.Node(v, kids);
    }

    @Test
    void examples() {
        assertEquals(3, solution.maxDepth(n(1, n(3, n(5), n(6)), n(2), n(4))));
        assertEquals(0, solution.maxDepth(null));
        assertEquals(1, solution.maxDepth(n(1)));
        assertEquals(5, solution.maxDepth(n(1, n(2), n(3, n(6), n(7, n(11, n(14)))), n(4, n(8, n(12))), n(5, n(9, n(13)), n(10)))));
    }
}
