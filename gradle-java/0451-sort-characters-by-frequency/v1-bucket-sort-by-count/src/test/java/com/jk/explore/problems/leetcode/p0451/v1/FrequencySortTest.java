package com.jk.explore.problems.leetcode.p0451.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FrequencySortTest {

    private final FrequencySort solution = new FrequencySort();

    @ParameterizedTest
    @CsvSource({"tree,eert", "cccaaa,aaaccc", "Aabb,bbAa", "a,a", "2a554442,4442255a"})
    void sorts(String s, String expected) {
        assertEquals(expected, solution.frequencySort(s));
    }
}
