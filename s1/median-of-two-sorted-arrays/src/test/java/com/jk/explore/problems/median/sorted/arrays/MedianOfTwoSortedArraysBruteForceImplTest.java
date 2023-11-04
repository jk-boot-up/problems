package com.jk.explore.problems.median.sorted.arrays;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MedianOfTwoSortedArraysBruteForceImplTest {

    private MedianOfTwoSortedArrays cut;

    @BeforeEach
    void setUp() {
        cut = new MedianOfTwoSortedArraysBruteForceImpl();
    }

    @Test
    void median1() {
        int[] a = new int[] {1, 5, 20, 47};
        int[] b = new int[] {2, 4, 25, 50};
        // 1, 2, 4, 5, 20, 25, 47, 50
        // (5 + 20) / 2 = 12.5
        double actual = cut.median(a, b);
        assertEquals(12.5, actual);
    }

    @Test
    void median2() {
        int[] a = new int[] {1, 5};
        int[] b = new int[] {3, 6, 20, 40, 50, 56};
        // 1, 3, 5, 6, 20, 40, 50, 56
        // (6 + 20) / 2 = 13
        double actual = cut.median(a, b);
        assertEquals(13, actual);
    }

    @Test
    void median3() {
        int[] a = new int[] {1, 5};
        int[] b = new int[] {7};
        // 1, 5, 7
        // 5
        double actual = cut.median(a, b);
        assertEquals(5, actual);
    }

    @Test
    void median4() {
        int[] a = new int[] {1};
        int[] b = new int[] {5, 7};
        // 1, 5, 7
        // 5
        double actual = cut.median(a, b);
        assertEquals(5, actual);
    }

    @Test
    void median5() {
        int[] a = new int[] {1, 5};
        int[] b = new int[] {5, 7};
        // 1, 5, 5, 7
        // 5
        double actual = cut.median(a, b);
        assertEquals(5, actual);
    }

    @Test
    void median6() {
        int[] a = new int[] {1, 5, 6};
        int[] b = new int[] {8, 7};
        // 1, 5, 6, 7, 8
        // 6
        double actual = cut.median(a, b);
        assertEquals(6, actual);
    }


}
