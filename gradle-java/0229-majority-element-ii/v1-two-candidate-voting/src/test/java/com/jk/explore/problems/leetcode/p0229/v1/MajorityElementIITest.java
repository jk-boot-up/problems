package com.jk.explore.problems.leetcode.p0229.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MajorityElementIITest {

    private final MajorityElementII solution = new MajorityElementII();

    @Test
    void examples() {
        assertEquals(List.of(3), solution.majorityElement(new int[]{3, 2, 3}));
        assertEquals(List.of(1), solution.majorityElement(new int[]{1}));
        assertEquals(Set.of(1, 2), new HashSet<>(solution.majorityElement(new int[]{1, 2})));
    }

    @Test
    void zeros() {
        assertEquals(List.of(0), solution.majorityElement(new int[]{0, 0, 0}));
    }
}
