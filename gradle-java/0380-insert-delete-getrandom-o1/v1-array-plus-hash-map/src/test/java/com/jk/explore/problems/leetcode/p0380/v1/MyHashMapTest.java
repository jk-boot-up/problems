package com.jk.explore.problems.leetcode.p0380.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MyHashMapTest {

    @Test
    void putGetOverwriteRemove() {
        MyHashMap<String, Integer> map = new MyHashMap<>();
        assertNull(map.put("a", 1));
        assertEquals(1, map.put("a", 2));
        assertEquals(2, map.get("a"));
        assertTrue(map.containsKey("a"));
        assertEquals(2, map.remove("a"));
        assertFalse(map.containsKey("a"));
        assertNull(map.remove("a"));
        assertTrue(map.isEmpty());
    }

    @Test
    void survivesResizingAndCollisions() {
        MyHashMap<Integer, Integer> map = new MyHashMap<>();
        for (int i = 0; i < 10_000; i++) map.put(i * 64, i); // multiples of 64 share low bits
        assertEquals(10_000, map.size());
        for (int i = 0; i < 10_000; i++) assertEquals(i, map.get(i * 64));
        for (int i = 0; i < 10_000; i += 2) map.remove(i * 64);
        assertEquals(5_000, map.size());
        assertNull(map.get(0));
        assertEquals(1, map.get(64));
    }

    @Test
    void helpersAndNullKey() {
        MyHashMap<String, Integer> map = new MyHashMap<>();
        assertEquals(1, map.merge("x", 1, Integer::sum));
        assertEquals(3, map.merge("x", 2, Integer::sum));
        assertEquals(7, map.getOrDefault("y", 7));
        assertEquals(3, map.putIfAbsent("x", 9));
        assertEquals(0, map.computeIfAbsent("z", k -> 0));
        map.put(null, 5);
        assertEquals(5, map.get(null));
        assertEquals(3, map.keys().size()); // x, z and null
    }

    @Test
    void hashSet() {
        MyHashSet<Character> set = new MyHashSet<>();
        assertTrue(set.add('a'));
        assertFalse(set.add('a'));
        assertTrue(set.contains('a'));
        assertTrue(set.remove('a'));
        assertFalse(set.contains('a'));
        assertEquals(0, set.size());
    }
}
