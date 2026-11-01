package com.jk.explore.problems.leetcode.p0589.v1;

import java.util.*;

public class NaryPreorder {

    public static final class Node {
        public int val;
        public List<Node> children;

        public Node(int val, Node... children) {
            this.val = val;
            this.children = new ArrayList<>(List.of(children));
        }
    }

    public List<Integer> preorder(Node root) {
        List<Integer> out = new ArrayList<>();
        if (root == null) return out;
        Deque<Node> stack = new ArrayDeque<>(List.of(root));
        while (!stack.isEmpty()) {
            Node n = stack.pop();
            out.add(n.val);
            for (int i = n.children.size() - 1; i >= 0; i--) stack.push(n.children.get(i));
        }
        return out;
    }
}
