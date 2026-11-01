package com.jk.explore.problems.leetcode.p0295.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MedianFinderTest {

    @Test
    void example() {
        MedianFinder m = new MedianFinder();
        m.addNum(1);
        m.addNum(2);
        assertEquals(1.5, m.findMedian());
        m.addNum(3);
        assertEquals(2.0, m.findMedian());
    }

    @Test
    void unsortedStream() {
        MedianFinder m = new MedianFinder();
        int[] stream = {5, 15, 1, 3, 8, 7, 9, 10};
        double[] expected = {5, 10, 5, 4, 5, 6, 7, 7.5};
        for (int i = 0; i < stream.length; i++) {
            m.addNum(stream[i]);
            assertEquals(expected[i], m.findMedian());
        }
    }
}
