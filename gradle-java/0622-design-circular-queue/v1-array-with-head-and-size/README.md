# 622. Design Circular Queue — v1: Array with head and size

**Difficulty:** Medium &nbsp;|&nbsp; **Topic:** Design &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/design-circular-queue/)

## Problem

Implement a fixed-capacity circular queue:

* `MyCircularQueue(int k)`
* `boolean enQueue(int value)`, `boolean deQueue()` — return `false` when full / empty.
* `int Front()`, `int Rear()` — return `-1` when empty.
* `boolean isEmpty()`, `boolean isFull()`

**Example**
```
k = 3: enQueue(1) true, enQueue(2) true, enQueue(3) true, enQueue(4) false,
Rear() 3, isFull() true, deQueue() true, enQueue(4) true, Rear() 4
```

**Constraints**
* `1 <= k <= 1000`, up to 3000 calls

## Approach: Array with head and size

> A fixed array with a head index and a size; the tail position is (head + size) mod capacity.

**Ring buffer.** Store `head` (index of the front) and `size`. The next free slot is `(head + size) % k` and the rear is
`(head + size - 1) % k`. Dequeue just moves `head` forward. Tracking `size` separates "full" from "empty", which both have head == tail.

* Time: **O(1)** — every operation.
* Space: **O(k)** — the array.

## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/com/jk/explore/problems/leetcode/p0622/v1/MyCircularQueue.java` | Solution |
| `src/test/java/com/jk/explore/problems/leetcode/p0622/v1/MyCircularQueueTest.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle 9.8.2 project. Only a JDK is needed to start Gradle; JDK 25 is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves.

Switch between Light, Medium and Dark themes in the header.
