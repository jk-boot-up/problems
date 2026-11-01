package com.jk.explore.problems.leetcode.p0382.v2;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class LinkedListRandomNodeTest {

    @Test
    void singleNode() {
        assertEquals(5, new LinkedListRandomNode(ListNode.of(5)).getRandom());
    }

    @Test
    void roughlyUniform() {
        LinkedListRandomNode s = new LinkedListRandomNode(ListNode.of(1, 2, 3, 4), new Random(42));
        int[] seen = new int[5];
        int draws = 40_000;
        for (int i = 0; i < draws; i++) seen[s.getRandom()]++;
        for (int v = 1; v <= 4; v++) assertEquals(draws / 4.0, seen[v], draws * 0.02, "value " + v);
    }
}
