package com.jk.explore.problems.median.sorted.arrays;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.io.StreamTokenizer;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;
import java.util.stream.Stream;

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

    @Test
    void median2() {
        int[] a = { 1, 2, 3, 4 };
        int[] b = { 5, 6, 7, 8};

        // sorted: -12, -10, -6, -5, -3, 3, 4, 6, 10, 12, 15

        double median = cut.median(a, b);
        assertEquals(4.5, median);
    }

    @Test
    void test2() {
        String input = "1010:Vivek :| 3010: Amex :| 2010: Interview :| 4010: NA";

//        StringTokenizer stringTokenizer = new StringTokenizer(input, ":|");
//        List<String> tokens = new ArrayList<>();
//        while(stringTokenizer.hasMoreTokens()) {
//            stringTokenizer.nextToken();
//        }
//        String [] inputTokens = stringTokenizer.toke
        Stream.of(input.split(":|")).collect(Collectors.toList());
    }




}
