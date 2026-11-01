package com.jk.explore.problems.leetcode.p0307.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class NumArrayTest {

    @Test
    void example() {
        NumArray a = new NumArray(new int[]{1, 3, 5});
        assertEquals(9, a.sumRange(0, 2));
        a.update(1, 2);
        assertEquals(8, a.sumRange(0, 2));
        assertEquals(2, a.sumRange(1, 1));
    }

    @Test
    void matchesBruteForce() {
        Random rnd = new Random(7);
        int[] ref = new int[50];
        for (int i = 0; i < ref.length; i++) ref[i] = rnd.nextInt(201) - 100;
        NumArray a = new NumArray(ref);
        for (int step = 0; step < 2000; step++) {
            if (rnd.nextBoolean()) {
                int i = rnd.nextInt(ref.length), v = rnd.nextInt(201) - 100;
                ref[i] = v;
                a.update(i, v);
            } else {
                int l = rnd.nextInt(ref.length), r = l + rnd.nextInt(ref.length - l), s = 0;
                for (int i = l; i <= r; i++) s += ref[i];
                assertEquals(s, a.sumRange(l, r));
            }
        }
    }
}
