package com.jk.explore.problems.leetcode.p0116.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class PopulatingNextRightPerfectTest {

    private final PopulatingNextRightPerfect solution = new PopulatingNextRightPerfect();

    @Test
    void perfectTree() {
        PopulatingNextRightPerfect.Node[] n = new PopulatingNextRightPerfect.Node[8];
        for (int i = 7; i >= 1; i--) n[i] = new PopulatingNextRightPerfect.Node(i, 2 * i < 8 ? n[2 * i] : null, 2 * i + 1 < 8 ? n[2 * i + 1] : null);
        solution.connect(n[1]);
        assertNull(n[1].next);
        assertSame(n[3], n[2].next);
        assertSame(n[5], n[4].next);
        assertSame(n[6], n[5].next);
        assertSame(n[7], n[6].next);
        assertNull(n[7].next);
    }
}
