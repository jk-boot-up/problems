package com.jk.explore.problems.leetcode.p0589.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NaryPreorderTest {

    private final NaryPreorder solution = new NaryPreorder();

    private static NaryPreorder.Node n(int v, NaryPreorder.Node... kids) {
        return new NaryPreorder.Node(v, kids);
    }

    @Test
    void examples() {
        assertEquals(List.of(1, 3, 5, 6, 2, 4), solution.preorder(n(1, n(3, n(5), n(6)), n(2), n(4))));
        assertEquals(List.of(), solution.preorder(null));
        assertEquals(List.of(1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10),
                solution.preorder(n(1, n(2), n(3, n(6), n(7, n(11, n(14)))), n(4, n(8, n(12))), n(5, n(9, n(13)), n(10)))));
    }
}
