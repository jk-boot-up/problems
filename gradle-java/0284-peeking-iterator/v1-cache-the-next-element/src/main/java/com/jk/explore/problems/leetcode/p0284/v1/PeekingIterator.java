package com.jk.explore.problems.leetcode.p0284.v1;

import java.util.*;

public class PeekingIterator implements Iterator<Integer> {

    private final Iterator<Integer> inner;
    private Integer ahead;
    private boolean hasAhead;

    public PeekingIterator(Iterator<Integer> iterator) {
        inner = iterator;
        advance();
    }

    private void advance() {
        hasAhead = inner.hasNext();
        ahead = hasAhead ? inner.next() : null;
    }

    public Integer peek() {
        return ahead;
    }

    @Override
    public Integer next() {
        if (!hasAhead) throw new NoSuchElementException();
        Integer v = ahead;
        advance();
        return v;
    }

    @Override
    public boolean hasNext() {
        return hasAhead;
    }
}
