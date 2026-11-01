package com.jk.explore.problems.leetcode.p0341.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NestedIteratorTest {

    private static NestedInteger i(int v) { return NestedInteger.of(v); }

    private static NestedInteger l(NestedInteger... items) { return NestedInteger.list(items); }

    private List<Integer> drain(List<NestedInteger> input) {
        NestedIterator it = new NestedIterator(input);
        List<Integer> out = new ArrayList<>();
        while (it.hasNext()) out.add(it.next());
        return out;
    }

    @Test
    void examples() {
        assertEquals(List.of(1, 1, 2, 1, 1), drain(List.of(l(i(1), i(1)), i(2), l(i(1), i(1)))));
        assertEquals(List.of(1, 4, 6), drain(List.of(i(1), l(i(4), l(i(6))))));
        assertEquals(List.of(), drain(List.of(l(), l(l()))));
        assertEquals(List.of(0, -3), drain(List.of(l(l(l(i(0)))), l(), i(-3))));
    }
}
