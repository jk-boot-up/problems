package com.jk.explore.problems.leetcode.p0706.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class DesignHashMapTest {

    @Test
    void example() {
        DesignHashMap m = new DesignHashMap();
        m.put(1, 1);
        m.put(2, 2);
        assertEquals(1, m.get(1));
        assertEquals(-1, m.get(3));
        m.put(2, 1);
        assertEquals(1, m.get(2));
        m.remove(2);
        assertEquals(-1, m.get(2));
    }

    @Test
    void manyKeysAndCollisions() {
        DesignHashMap m = new DesignHashMap();
        for (int k = 0; k < 5000; k++) m.put(k * 16, k);
        for (int k = 0; k < 5000; k++) assertEquals(k, m.get(k * 16));
        for (int k = 0; k < 5000; k += 2) m.remove(k * 16);
        assertEquals(-1, m.get(0));
        assertEquals(1, m.get(16));
    }
}
