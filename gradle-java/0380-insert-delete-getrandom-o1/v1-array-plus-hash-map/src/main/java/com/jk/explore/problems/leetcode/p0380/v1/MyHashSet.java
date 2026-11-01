package com.jk.explore.problems.leetcode.p0380.v1;


/**
 * A hash set written from scratch (no java.util.HashSet): it is a {@link MyHashMap} whose keys are the elements
 * and whose values are ignored, so it inherits the bucket array, chaining and resizing.
 *
 * @param <E> element type
 */
public class MyHashSet<E> implements Iterable<E> {

    private static final Object PRESENT = new Object();
    private final MyHashMap<E, Object> map = new MyHashMap<>();

    /** Adds e; returns true if it was not already present. */
    public boolean add(E e) {
        return map.put(e, PRESENT) == null;
    }

    public boolean contains(Object e) {
        return map.containsKey(e);
    }

    /** Removes e; returns true if it was present. */
    public boolean remove(Object e) {
        return map.remove(e) != null;
    }

    public int size() { return map.size(); }

    public boolean isEmpty() { return map.isEmpty(); }

    public void clear() { map.clear(); }

    @Override
    public java.util.Iterator<E> iterator() {
        return map.keys().iterator();
    }
}
