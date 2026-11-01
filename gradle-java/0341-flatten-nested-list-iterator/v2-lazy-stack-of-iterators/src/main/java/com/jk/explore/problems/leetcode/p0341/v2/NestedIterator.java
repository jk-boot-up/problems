package com.jk.explore.problems.leetcode.p0341.v2;

import java.util.*;

interface NestedInteger {

    boolean isInteger();

    Integer getInteger();

    List<NestedInteger> getList();

    static NestedInteger of(int value) {
        return new NestedInteger() {
            public boolean isInteger() { return true; }
            public Integer getInteger() { return value; }
            public List<NestedInteger> getList() { return null; }
        };
    }

    static NestedInteger list(NestedInteger... items) {
        List<NestedInteger> l = List.of(items);
        return new NestedInteger() {
            public boolean isInteger() { return false; }
            public Integer getInteger() { return null; }
            public List<NestedInteger> getList() { return l; }
        };
    }
}

public class NestedIterator implements Iterator<Integer> {

    private final Deque<Iterator<NestedInteger>> stack = new ArrayDeque<>();
    private Integer ready;

    public NestedIterator(List<NestedInteger> nestedList) {
        stack.push(nestedList.iterator());
    }

    @Override
    public boolean hasNext() {
        while (ready == null && !stack.isEmpty()) {
            Iterator<NestedInteger> top = stack.peek();
            if (!top.hasNext()) {
                stack.pop();
                continue;
            }
            NestedInteger item = top.next();
            if (item.isInteger()) ready = item.getInteger();
            else stack.push(item.getList().iterator());
        }
        return ready != null;
    }

    @Override
    public Integer next() {
        if (!hasNext()) throw new NoSuchElementException();
        Integer v = ready;
        ready = null;
        return v;
    }
}
