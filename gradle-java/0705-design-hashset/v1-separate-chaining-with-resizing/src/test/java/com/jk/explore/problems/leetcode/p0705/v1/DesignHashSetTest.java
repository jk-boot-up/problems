package com.jk.explore.problems.leetcode.p0705.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DesignHashSetTest {

    @Test
    void example() {
        DesignHashSet s = new DesignHashSet();
        s.add(1);
        s.add(2);
        assertTrue(s.contains(1));
        assertFalse(s.contains(3));
        s.add(2);
        assertTrue(s.contains(2));
        s.remove(2);
        assertFalse(s.contains(2));
        s.remove(42);
    }

    @Test
    void many() {
        DesignHashSet s = new DesignHashSet();
        for (int k = 0; k < 3000; k++) s.add(k * 32);
        for (int k = 0; k < 3000; k++) assertTrue(s.contains(k * 32));
        assertFalse(s.contains(1));
    }
}
