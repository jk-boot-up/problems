package com.jk.explore.problems.median.sorted.arrays;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class MedianOfTwoSortedArraysBinarySearchImplTest {

    private MedianOfTwoSortedArraysBinarySearchImpl cut;

    @BeforeEach
    void setUp() {
        cut = new MedianOfTwoSortedArraysBinarySearchImpl();
    }

    @Test
    void median1() {
        int[] a = { -5, 3, 6, 12, 15 };
        int[] b = { -12, -10, -6, -3, 4, 10 };

        // sorted: -12, -10, -6, -5, -3, 3, 4, 6, 10, 12, 15

        double median = cut.median(a, b);
        assertEquals(3.0, median);
    }



}
