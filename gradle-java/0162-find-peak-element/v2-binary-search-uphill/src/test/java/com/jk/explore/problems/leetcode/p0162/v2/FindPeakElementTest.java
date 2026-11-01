package com.jk.explore.problems.leetcode.p0162.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class FindPeakElementTest {

    private final FindPeakElement solution = new FindPeakElement();

    private static boolean isPeak(int[] a, int i) {
        return (i == 0 || a[i] > a[i - 1]) && (i == a.length - 1 || a[i] > a[i + 1]);
    }

    @Test
    void examples() {
        int[] a = {1, 2, 3, 1};
        assertEquals(2, solution.findPeakElement(a));
        int[] b = {1, 2, 1, 3, 5, 6, 4};
        assertTrue(isPeak(b, solution.findPeakElement(b)));
    }

    @Test
    void edges() {
        assertEquals(0, solution.findPeakElement(new int[]{1}));
        assertEquals(0, solution.findPeakElement(new int[]{3, 2, 1}));
        assertEquals(2, solution.findPeakElement(new int[]{1, 2, 3}));
    }
}
