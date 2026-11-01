package com.jk.explore.problems.leetcode.p0297.v1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class CodecTest {

    private final Codec codec = new Codec();

    @Test
    void roundTrip() {
        TreeNode root = TreeNode.of(1, 2, 3, null, null, 4, 5);
        String s = codec.serialize(root);
        assertEquals("1,2,#,#,3,4,#,#,5,#,#", s);
        assertEquals(TreeNode.toList(root), TreeNode.toList(codec.deserialize(s)));
    }

    @Test
    void empty() {
        assertNull(codec.deserialize(codec.serialize(null)));
    }

    @Test
    void negatives() {
        TreeNode root = TreeNode.of(-1, null, -2, -3);
        assertEquals(TreeNode.toList(root), TreeNode.toList(codec.deserialize(codec.serialize(root))));
    }
}
