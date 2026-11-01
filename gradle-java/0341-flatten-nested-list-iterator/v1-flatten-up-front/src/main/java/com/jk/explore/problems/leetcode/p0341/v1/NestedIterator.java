package com.jk.explore.problems.leetcode.p0341.v1;

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

    private final List<Integer> flat = new ArrayList<>();
    private int pos;

    public NestedIterator(List<NestedInteger> nestedList) {
        flatten(nestedList);
    }

    private void flatten(List<NestedInteger> list) {
        for (NestedInteger item : list) {
            if (item.isInteger()) flat.add(item.getInteger());
            else flatten(item.getList());
        }
    }

    @Override
    public boolean hasNext() {
        return pos < flat.size();
    }

    @Override
    public Integer next() {
        if (!hasNext()) throw new NoSuchElementException();
        return flat.get(pos++);
    }
}
