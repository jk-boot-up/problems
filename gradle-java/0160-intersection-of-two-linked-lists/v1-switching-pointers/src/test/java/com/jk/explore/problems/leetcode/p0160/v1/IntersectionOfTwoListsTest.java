package com.jk.explore.problems.leetcode.p0160.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class IntersectionOfTwoListsTest {

    private final IntersectionOfTwoLists solution = new IntersectionOfTwoLists();

    @Test
    void shared() {
        ListNode shared = ListNode.of(8, 4, 5);
        ListNode a = new ListNode(4, new ListNode(1, shared));
        ListNode b = new ListNode(5, new ListNode(6, new ListNode(1, shared)));
        assertSame(shared, solution.getIntersectionNode(a, b));
    }

    @Test
    void disjoint() {
        assertNull(solution.getIntersectionNode(ListNode.of(2, 6, 4), ListNode.of(1, 5)));
    }
}
