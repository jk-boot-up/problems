package com.jk.explore.problems.leetcode.p0380.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RandomizedSetTest {

    @Test
    void exampleSequence() {
        RandomizedSet set = new RandomizedSet();
        assertTrue(set.insert(1));
        assertFalse(set.remove(2));
        assertTrue(set.insert(2));
        assertTrue(Set.of(1, 2).contains(set.getRandom()));
        assertTrue(set.remove(1));
        assertFalse(set.insert(2));
        assertEquals(2, set.getRandom());
    }

    @Test
    void removeMiddleKeepsOthers() {
        RandomizedSet set = new RandomizedSet(new Random(1));
        for (int i = 0; i < 5; i++) set.insert(i);
        assertTrue(set.remove(2));
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < 200; i++) seen.add(set.getRandom());
        assertEquals(Set.of(0, 1, 3, 4), seen);
    }
}
