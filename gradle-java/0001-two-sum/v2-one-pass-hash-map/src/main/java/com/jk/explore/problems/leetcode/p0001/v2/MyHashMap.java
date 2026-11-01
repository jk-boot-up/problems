package com.jk.explore.problems.leetcode.p0001.v2;


/**
 * A hash map written from scratch (no java.util.HashMap), showing the core idea:
 *
 * <ol>
 *   <li><b>Buckets:</b> an array of slots. A key's hash code picks the slot: {@code index = spread(hash) & (capacity - 1)}.
 *       The capacity is a power of two, so the AND keeps the low bits and acts as a cheap modulo.</li>
 *   <li><b>Spreading:</b> {@code h ^ (h >>> 16)} mixes the high bits into the low bits, so keys whose hash codes differ
 *       only in high bits still land in different buckets.</li>
 *   <li><b>Collisions:</b> keys that land in the same bucket are chained in a singly linked list.</li>
 *   <li><b>Resizing:</b> when size exceeds capacity × 0.75 the array doubles and every entry is re-bucketed, which
 *       keeps chains short, so get/put/remove stay O(1) on average.</li>
 * </ol>
 *
 * @param <K> key type (must implement equals/hashCode consistently; null keys are allowed)
 * @param <V> value type
 */
public class MyHashMap<K, V> {

    /** One key/value pair in a bucket's chain. */
    public static final class Entry<K, V> {
        final K key;
        final int hash;
        V value;
        Entry<K, V> next;

        Entry(K key, int hash, V value, Entry<K, V> next) {
            this.key = key;
            this.hash = hash;
            this.value = value;
            this.next = next;
        }

        public K getKey() { return key; }

        public V getValue() { return value; }
    }

    private static final int INITIAL_CAPACITY = 16;
    private static final float LOAD_FACTOR = 0.75f;

    private Entry<K, V>[] buckets;
    private int size;

    public MyHashMap() {
        this(INITIAL_CAPACITY);
    }

    @SuppressWarnings("unchecked")
    public MyHashMap(int expectedSize) {
        int capacity = 1;
        while (capacity < expectedSize / LOAD_FACTOR + 1) capacity <<= 1;
        buckets = (Entry<K, V>[]) new Entry[Math.max(capacity, 2)];
    }

    /** Mixes the high bits of the hash code into the low bits. */
    private static int spread(Object key) {
        int h = key == null ? 0 : key.hashCode();
        return h ^ (h >>> 16);
    }

    private int indexFor(int hash) {
        return hash & (buckets.length - 1);
    }

    private Entry<K, V> find(Object key) {
        int hash = spread(key);
        for (Entry<K, V> e = buckets[indexFor(hash)]; e != null; e = e.next) {
            if (e.hash == hash && (e.key == key || (key != null && key.equals(e.key)))) return e;
        }
        return null;
    }

    public V get(Object key) {
        Entry<K, V> e = find(key);
        return e == null ? null : e.value;
    }

    public V getOrDefault(Object key, V defaultValue) {
        Entry<K, V> e = find(key);
        return e == null ? defaultValue : e.value;
    }

    public boolean containsKey(Object key) {
        return find(key) != null;
    }

    /** Associates value with key; returns the previous value, or null if the key was absent. */
    public V put(K key, V value) {
        Entry<K, V> e = find(key);
        if (e != null) {
            V old = e.value;
            e.value = value;
            return old;
        }
        int hash = spread(key);
        int i = indexFor(hash);
        buckets[i] = new Entry<>(key, hash, value, buckets[i]); // prepend to the chain
        if (++size > buckets.length * LOAD_FACTOR) resize();
        return null;
    }

    /** Puts only if the key is absent; returns the existing value, or null if it was inserted. */
    public V putIfAbsent(K key, V value) {
        Entry<K, V> e = find(key);
        if (e != null) return e.value;
        put(key, value);
        return null;
    }

    /** If absent, stores value; otherwise stores fn(old, value). Returns the new value. */
    public V merge(K key, V value, java.util.function.BinaryOperator<V> fn) {
        Entry<K, V> e = find(key);
        if (e == null) {
            put(key, value);
            return value;
        }
        e.value = fn.apply(e.value, value);
        return e.value;
    }

    /** Returns the value for key, creating it with factory first if the key is absent. */
    public V computeIfAbsent(K key, java.util.function.Function<K, V> factory) {
        Entry<K, V> e = find(key);
        if (e != null) return e.value;
        V v = factory.apply(key);
        put(key, v);
        return v;
    }

    /** Removes key; returns its value, or null if it was absent. */
    public V remove(Object key) {
        int hash = spread(key);
        int i = indexFor(hash);
        Entry<K, V> prev = null;
        for (Entry<K, V> e = buckets[i]; e != null; prev = e, e = e.next) {
            if (e.hash == hash && (e.key == key || (key != null && key.equals(e.key)))) {
                if (prev == null) buckets[i] = e.next; else prev.next = e.next;
                size--;
                return e.value;
            }
        }
        return null;
    }

    public int size() { return size; }

    public boolean isEmpty() { return size == 0; }

    @SuppressWarnings("unchecked")
    public void clear() {
        buckets = (Entry<K, V>[]) new Entry[INITIAL_CAPACITY];
        size = 0;
    }

    /** Doubles the bucket array and moves every entry to its bucket in the new array. */
    @SuppressWarnings("unchecked")
    private void resize() {
        Entry<K, V>[] old = buckets;
        buckets = (Entry<K, V>[]) new Entry[old.length * 2];
        for (Entry<K, V> head : old) {
            for (Entry<K, V> e = head; e != null; ) {
                Entry<K, V> next = e.next;
                int i = indexFor(e.hash);
                e.next = buckets[i];
                buckets[i] = e;
                e = next;
            }
        }
    }

    /** All entries, bucket by bucket. */
    public java.util.List<Entry<K, V>> entries() {
        java.util.List<Entry<K, V>> out = new java.util.ArrayList<>(size);
        for (Entry<K, V> head : buckets) {
            for (Entry<K, V> e = head; e != null; e = e.next) out.add(e);
        }
        return out;
    }

    public java.util.List<K> keys() {
        java.util.List<K> out = new java.util.ArrayList<>(size);
        for (Entry<K, V> e : entries()) out.add(e.key);
        return out;
    }

    public java.util.List<V> values() {
        java.util.List<V> out = new java.util.ArrayList<>(size);
        for (Entry<K, V> e : entries()) out.add(e.value);
        return out;
    }
}
