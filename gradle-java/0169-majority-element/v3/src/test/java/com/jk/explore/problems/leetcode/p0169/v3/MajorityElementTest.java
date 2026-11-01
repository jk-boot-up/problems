package com.jk.explore.problems.leetcode.p0169.v3;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MajorityElementTest {

    private final MajorityElement solution = new MajorityElement();

    @Test
    void example1() {
        assertEquals(3, solution.majorityElement(new int[]{3, 2, 3}));
    }

    @Test
    void example2() {
        assertEquals(2, solution.majorityElement(new int[]{2, 2, 1, 1, 1, 2, 2}));
    }

    @Test
    void single() {
        assertEquals(-7, solution.majorityElement(new int[]{-7}));
    }
}
