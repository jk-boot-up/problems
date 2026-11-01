package com.jk.explore.problems.leetcode.p0075.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class SortColorsTest {

    private final SortColors solution = new SortColors();

    @Test
    void examples() {
        int[] a = {2, 0, 2, 1, 1, 0};
        solution.sortColors(a);
        assertArrayEquals(new int[]{0, 0, 1, 1, 2, 2}, a);
        int[] b = {2, 0, 1};
        solution.sortColors(b);
        assertArrayEquals(new int[]{0, 1, 2}, b);
    }
}
