package com.jk.explore.problems.leetcode.p0427.v1;

import java.util.*;

public class ConstructQuadTree {

    /** Quad tree node. */
    public static class Node {
        public boolean val, isLeaf;
        public Node topLeft, topRight, bottomLeft, bottomRight;

        public Node(boolean val, boolean isLeaf) {
            this.val = val;
            this.isLeaf = isLeaf;
        }

        public Node(boolean val, boolean isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
            this(val, isLeaf);
            this.topLeft = topLeft;
            this.topRight = topRight;
            this.bottomLeft = bottomLeft;
            this.bottomRight = bottomRight;
        }
    }

    public Node construct(int[][] grid) {
        return build(grid, 0, 0, grid.length);
    }

    private Node build(int[][] g, int r, int c, int size) {
        if (size == 1) return new Node(g[r][c] == 1, true);
        int h = size / 2;
        Node tl = build(g, r, c, h), tr = build(g, r, c + h, h), bl = build(g, r + h, c, h), br = build(g, r + h, c + h, h);
        if (tl.isLeaf && tr.isLeaf && bl.isLeaf && br.isLeaf && tl.val == tr.val && tr.val == bl.val && bl.val == br.val) {
            return new Node(tl.val, true);
        }
        return new Node(true, false, tl, tr, bl, br);
    }
}
