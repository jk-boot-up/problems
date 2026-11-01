package com.jk.explore.problems.leetcode.p0071.v1;

import java.util.*;

public class SimplifyPath {

    public String simplifyPath(String path) {
        Deque<String> stack = new ArrayDeque<>();
        for (String part : path.split("/")) {
            if (part.isEmpty() || part.equals(".")) continue;
            if (part.equals("..")) {
                stack.pollLast();
            } else {
                stack.addLast(part);
            }
        }
        return "/" + String.join("/", stack);
    }
}
