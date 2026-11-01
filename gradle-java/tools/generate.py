#!/usr/bin/env python3
"""Generates one standalone Gradle build per LeetCode problem, with one subproject per solution version.

Problem data lives in tools/problems/batch_*.py. Each batch defines a list PROBLEMS of
dicts created with P(...). Run from anywhere:  python3 gradle-java/tools/generate.py
"""
import html
import json
import re
import importlib.util
import os
import shutil
import stat
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent  # gradle-java/
BASE_PKG = "com.jk.explore.problems.leetcode"
JUNIT = "6.1.3"
GRADLE = "9.8.2"
JAVA = 25

SOLUTION_IMPORTS = "import java.util.*;\n"
TEST_IMPORTS = """import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;
"""

LIST_NODE = """/** Singly linked list node used by the LeetCode list problems. */
public class ListNode {
    public int val;
    public ListNode next;

    public ListNode(int val) { this.val = val; }

    public ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    /** Builds a list from the given values and returns its head (null when empty). */
    public static ListNode of(int... values) {
        ListNode dummy = new ListNode(0), tail = dummy;
        for (int v : values) { tail.next = new ListNode(v); tail = tail.next; }
        return dummy.next;
    }

    /** Converts the list starting at head to an int array. */
    public static int[] toArray(ListNode head) {
        List<Integer> out = new ArrayList<>();
        for (ListNode n = head; n != null; n = n.next) out.add(n.val);
        return out.stream().mapToInt(Integer::intValue).toArray();
    }
}
"""

TREE_NODE = """/** Binary tree node used by the LeetCode tree problems. */
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode(int val) { this.val = val; }

    public TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left = left; this.right = right; }

    /** Builds a tree from LeetCode level-order notation, e.g. of(3, 9, 20, null, null, 15, 7). */
    public static TreeNode of(Integer... values) {
        if (values.length == 0 || values[0] == null) return null;
        TreeNode root = new TreeNode(values[0]);
        Deque<TreeNode> queue = new ArrayDeque<>(List.of(root));
        int i = 1;
        while (!queue.isEmpty() && i < values.length) {
            TreeNode node = queue.poll();
            if (i < values.length && values[i] != null) { node.left = new TreeNode(values[i]); queue.add(node.left); }
            i++;
            if (i < values.length && values[i] != null) { node.right = new TreeNode(values[i]); queue.add(node.right); }
            i++;
        }
        return root;
    }

    /** Serializes a tree to LeetCode level-order notation with trailing nulls removed. */
    public static List<Integer> toList(TreeNode root) {
        List<Integer> out = new ArrayList<>();
        Deque<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            if (node == null) { out.add(null); continue; }
            out.add(node.val);
            queue.add(node.left);
            queue.add(node.right);
        }
        while (!out.isEmpty() && out.getLast() == null) out.removeLast();
        return out;
    }
}
"""

HELPERS = {"ListNode": LIST_NODE, "TreeNode": TREE_NODE,
           "MyHashMap": (TOOLS / "helpers" / "MyHashMap.java").read_text(),
           "MyHashSet": (TOOLS / "helpers" / "MyHashSet.java").read_text()}
HASH_TEST = (TOOLS / "helpers" / "MyHashMapTest.java").read_text()
# Solutions must use our own hash map / hash set, never the java.util ones.
FORBIDDEN = re.compile(r"\b(HashMap|HashSet|LinkedHashMap|LinkedHashSet|Hashtable|IdentityHashMap|WeakHashMap|ConcurrentHashMap)\b")


def helpers_for(v):
    hs = list(v["helpers"])
    if "MyHashMap" in v["java"] or "MyHashSet" in v["java"]:
        hs += [h for h in ("MyHashMap", "MyHashSet") if h not in hs]
    return hs

BUILD = f"""plugins {{
    java
}}

group = "{BASE_PKG}"
version = "1.0.0"

java {{
    toolchain {{
        languageVersion = JavaLanguageVersion.of({JAVA})
    }}
}}

repositories {{
    mavenCentral()
}}

dependencies {{
    testImplementation(platform("org.junit:junit-bom:{JUNIT}"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}}

tasks.test {{
    useJUnitPlatform()
    testLogging {{
        events("passed", "skipped", "failed")
    }}
}}
"""


SETTINGS = """plugins {
    // Downloads JDK __JAVA__ automatically if it is not installed locally.
    id("org.gradle.toolchains.foojay-resolver-convention") version "1.0.0"
}

rootProject.name = "__NAME__"
"""

GITIGNORE = ".gradle/\nbuild/\n.idea/\n*.iml\nout/\n"
MAX_VARIANTS = 5


def P(**kw):
    kw.setdefault("helpers", [])
    kw.setdefault("variants", [])
    kw.setdefault("vname", "Optimal")
    return kw


def variants(p):
    """Earlier, simpler variants first; the problem's own solution is the last (most efficient) version."""
    main = {k: p[k] for k in ("idea", "approach", "java", "trace")}
    main["name"] = p["vname"]
    vs = [dict(v) for v in p["variants"]] + [main]
    assert len(vs) <= MAX_VARIANTS, f"{p['num']}: at most {MAX_VARIANTS} variants"
    for i, v in enumerate(vs, 1):
        v["v"] = f"v{i}"
        v["dir"] = f"v{i}-" + re.sub(r"[^a-z0-9]+", "-", v["name"].lower().replace("–", "-")).strip("-")
        v.setdefault("test", p["test"])
        v.setdefault("helpers", p["helpers"])
        v["cx"] = complexity(v)
    return vs


def load_problems():
    probs = []
    for f in sorted((TOOLS / "problems").glob("batch_*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        mod.P = P
        spec.loader.exec_module(mod)
        probs.extend(mod.PROBLEMS)
    # extra solution versions kept in separate files: VARIANTS = {num: {"vname": ..., "variants": [...]}}
    by_num = {p["num"]: p for p in probs}
    for f in sorted((TOOLS / "problems").glob("variants_*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for num, extra in mod.VARIANTS.items():
            by_num[num].update(extra)
    return probs


def dir_name(p):
    return f"{p['num']:04d}-{p['slug']}"


def pkg(p, v):
    return f"{BASE_PKG}.p{p['num']:04d}.{v['v']}"


def write(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip("\n") + "\n", encoding="utf-8")


def java_file(p, v, body, imports):
    return f"package {pkg(p, v)};\n\n{imports}\n{body.strip()}\n"


def inline_md(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    return t


def md_to_html(text):
    """Small Markdown subset: headings, fenced code, bullet/numbered lists, bold, inline code, paragraphs."""
    out, para, lst, code = [], [], None, None
    def flush():
        nonlocal para, lst
        if para:
            out.append("<p>" + inline_md(" ".join(para)) + "</p>")
            para = []
        if lst:
            tag = lst[0]
            out.append(f"<{tag}>" + "".join(f"<li>{inline_md(i)}</li>" for i in lst[1]) + f"</{tag}>")
            lst = None
    for line in text.strip().splitlines():
        if code is not None:
            if line.strip().startswith("```"):
                out.append("<pre><code>" + html.escape("\n".join(code)) + "</code></pre>")
                code = None
            else:
                code.append(line)
            continue
        s = line.strip()
        if s.startswith("```"):
            flush(); code = []
        elif not s:
            flush()
        elif s.startswith("#"):
            flush(); lvl = len(s) - len(s.lstrip("#")); out.append(f"<h{lvl + 1}>{inline_md(s[lvl:].strip())}</h{lvl + 1}>")
        elif re.match(r"^[*-] ", s):
            if para: out.append("<p>" + inline_md(" ".join(para)) + "</p>"); para = []
            if not lst or lst[0] != "ul": flush(); lst = ("ul", [])
            lst[1].append(s[2:])
        elif re.match(r"^\d+\. ", s):
            if para: out.append("<p>" + inline_md(" ".join(para)) + "</p>"); para = []
            if not lst or lst[0] != "ol": flush(); lst = ("ol", [])
            lst[1].append(re.sub(r"^\d+\. ", "", s))
        elif lst and line.startswith("  "):
            lst[1][-1] += " " + s
        else:
            if lst: flush()
            para.append(s)
    flush()
    return "\n".join(out)


def cx_class(expr):
    e = expr.lower().replace(" ", "")
    inner = e[2:-1] if e.startswith("o(") else e
    if "2^" in e or "!" in e or "4^" in e or "3^" in e or "k^" in e: return "exp"
    if "²" in e or "^2" in e or re.search(r"[a-z]·[a-z]", inner) and "log" not in inner or "n*m" in inner or "m*n" in inner: return "n2"
    if "log" in inner:
        return "log" if re.fullmatch(r"log\w*\(?\w*\)?", inner) or re.fullmatch(r"log\(?[a-z·+]+\)?", inner) else "nlogn"
    if inner in ("1",): return "1"
    return "n"


def complexity(v):
    def grab(kind):
        m = re.search(kind + r":\s*\*\*(.+?)\*\*\s*(?:[—–-]+\s*(.*))?", v["approach"])
        return (m.group(1).strip(), (m.group(2) or "").strip()) if m else ("?", "")
    t, tw = grab("Time")
    s, sw = grab("Space")
    return {"time": t, "timeWhy": tw, "space": s, "spaceWhy": sw,
            "tc": v.get("tc") or cx_class(t), "sc": v.get("sc") or cx_class(s)}


def variant_nav(vs, cur):
    if len(vs) == 1:
        return ""
    links = "".join(
        f'<a class="{"on" if v["v"] == cur["v"] else ""}" href="../../{v["dir"]}/animation/index.html">{v["v"]} · {html.escape(v["name"])}</a>'
        for v in vs)
    return f'<nav class="variants" aria-label="Solution variants">{links}</nav>'


def compare_table(vs, cur):
    if len(vs) == 1:
        return ""
    rows = "".join(
        f'<tr class="{"on" if v["v"] == cur["v"] else ""}"><td><a href="../../{v["dir"]}/animation/index.html">{v["v"]}</a></td>'
        f'<td>{html.escape(v["name"])}</td><td><code>{html.escape(v["cx"]["time"])}</code></td><td><code>{html.escape(v["cx"]["space"])}</code></td></tr>'
        for v in vs)
    return f'<div class="card md" style="margin-top:18px"><h3>All variants of this problem</h3><table class="cmp"><tr><th>Version</th><th>Approach</th><th>Time</th><th>Space</th></tr>{rows}</table></div>'


def animation_html(p, vs, v, solution_src):
    css = (TOOLS / "engine" / "animator.css").read_text()
    js = (TOOLS / "engine" / "animator.js").read_text()
    cx = v["cx"]
    meta = {"num": p["num"], "title": p["title"], "idea": v["idea"], **cx}
    title = html.escape(p["title"])
    vlabel = f'<span class="vtag">{v["v"]} · {html.escape(v["name"])}</span>'
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{p['num']}. {title} ({v['v']}) · Animated walkthrough</title>
<style>
{css}</style>
</head>
<body>
<header>
  <div class="hwrap">
    <span class="hnum">#{p['num']}</span><h1>{title}</h1><span class="badge {p['diff']}">{p['diff']}</span><span class="topic">{html.escape(p['topic'])}</span>{vlabel}
    <span class="spacer"></span>
    <a class="lc" href="https://leetcode.com/problems/{p['slug']}/" target="_blank" rel="noopener">LeetCode ↗</a>
    <div class="themes" role="group" aria-label="Theme"><button data-theme="light">☀ Light</button><button data-theme="medium">◐ Medium</button><button data-theme="dark">☾ Dark</button></div>
  </div>
  <nav class="tabs">
    <button data-tab="problem" class="on"><span class="n">1</span>Problem</button>
    <button data-tab="walk"><span class="n">2</span>Walkthrough</button>
    <button data-tab="cx"><span class="n">3</span>Complexity</button>
    <span class="spacer"></span>{variant_nav(vs, v)}
  </nav>
</header>
<main>
  <section class="tab on" id="tab-problem">
    <div class="two">
      <div class="card md">{md_to_html(p['spec'])}</div>
      <div>
        <div class="card md">
          <h3>💡 Key idea ({v['v']} · {html.escape(v['name'])})</h3>
          <div class="idea">{html.escape(v['idea'])}</div>
          {md_to_html(v['approach'])}
          <div class="chips"><span class="chip">⏱ {html.escape(cx['time'])}</span><span class="chip">🧠 {html.escape(cx['space'])}</span><span class="chip">🎬 <span id="scount"></span>&nbsp;scenarios</span></div>
          <button class="cta" data-goto="walk">▶ Start the animated walkthrough</button>
        </div>
      </div>
    </div>
  </section>

  <section class="tab" id="tab-walk">
    <div class="scen" id="scen"></div>
    <section id="stage" aria-live="polite"></section>
    <div class="narr" id="narr"><span class="spk">🔊</span><span id="say"></span></div>
    <div id="controls">
      <button id="first" title="First step">⏮</button>
      <button id="prev" title="Previous step (←)">◀</button>
      <button id="play" class="primary" title="Play / pause (space)">▶ Play</button>
      <button id="next" title="Next step (→)">▶</button>
      <button id="last" title="Last step">⏭</button>
      <select id="speed" title="Speed"><option value="0.75">0.75×</option><option value="1" selected>1×</option><option value="1.25">1.25×</option><option value="1.5">1.5×</option><option value="2">2×</option></select>
      <button id="voiceOn" class="toggle on" aria-pressed="true" title="Turn spoken narration on or off (N)">🔊 Narration on</button>
      <select id="voice" title="Narrator voice (female voices marked ♀; Amy preferred when installed)"></select>
      <span id="counter"></span>
    </div>
    <div id="timeline" title="Jump to a step"></div>
    <div class="legend"><span style="--c:var(--cur)">current</span><span style="--c:var(--sel)">selected / window</span><span style="--c:var(--ok)">done / match</span><span style="--c:var(--bad)">rejected</span><span style="--c:var(--alt)">special</span></div>
    <div class="kbd"><kbd>Space</kbd> play/pause · <kbd>←</kbd> <kbd>→</kbd> step · <kbd>1</kbd>–<kbd>9</kbd> pick scenario · <kbd>N</kbd> narration on/off</div>
    <details class="code card"><summary>☕ Java solution ({v['v']})</summary><pre class="java"><code id="javacode">{html.escape(solution_src)}</code></pre></details>
  </section>

  <section class="tab" id="tab-cx">
    <div class="cxgrid" id="cx-cards"></div>
    {compare_table(vs, v)}
    <div class="card md" style="margin-top:18px"><h3>How the cost adds up</h3>{md_to_html(v['approach'])}</div>
  </section>
</main>
<script>
window.PROBLEM = {json.dumps(meta)};
{js}</script>
<script>
function trace(A) {{
{v['trace'].strip()}
}}
</script>
</body>
</html>
"""


def variants_table(p, vs, link_prefix=""):
    rows = "\n".join(
        f"| [{v['dir']}]({link_prefix}{v['dir']}/README.md) | {v['name']} | `{v['cx']['time']}` | `{v['cx']['space']}` | [▶ animation]({link_prefix}{v['dir']}/animation/index.html) |"
        for v in vs)
    return "| Project | Approach | Time | Space | Animation |\n|---------|----------|------|-------|-----------|\n" + rows


def problem_readme(p, vs):
    return f"""# {p['num']}. {p['title']}

**Difficulty:** {p['diff']} &nbsp;|&nbsp; **Topic:** {p['topic']} &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/{p['slug']}/)

## Problem

{p['spec'].strip()}

## Solutions

{"Each folder below is a separate, self-contained Gradle project, ordered from the simplest idea to the most efficient one." if len(vs) > 1 else "The folder below is a self-contained Gradle project."}
Open any of them on its own: it has its own Gradle wrapper, build files, README, tests and animation.

{variants_table(p, vs)}
"""


def variant_readme(p, vs, v):
    path = pkg(p, v).replace(".", "/")
    others = [o for o in vs if o is not v]
    see_also = ("\n## Other approaches\n\n" + "\n".join(f"* [{o['dir']}](../{o['dir']}/README.md): {o['name']} (`{o['cx']['time']}` time, `{o['cx']['space']}` space)" for o in others) + "\n") if others else ""
    hash_note = ("\nHash lookups use `MyHashMap` / `MyHashSet`, our own hash table (bucket array, chaining, resizing), "
                 "instead of `java.util.HashMap`.\n") if "MyHashMap" in helpers_for(v) else ""
    return f"""# {p['num']}. {p['title']} — {v['v']}: {v['name']}

**Difficulty:** {p['diff']} &nbsp;|&nbsp; **Topic:** {p['topic']} &nbsp;|&nbsp; [LeetCode](https://leetcode.com/problems/{p['slug']}/)

## Problem

{p['spec'].strip()}

## Approach: {v['name']}

> {v['idea']}

{v['approach'].strip()}
{hash_note}
## Project layout

| Path | Contents |
|------|----------|
| `src/main/java/{path}/{p['cls']}.java` | Solution |
| `src/test/java/{path}/{p['cls']}Test.java` | JUnit 6 tests |
| `animation/index.html` | Animated walkthrough with spoken narration |

## Build and test

This folder is a standalone Gradle {GRADLE} project. Only a JDK is needed to start Gradle; JDK {JAVA} is downloaded
automatically if it is missing.

```bash
./gradlew test
```

## Animation

Open [`animation/index.html`](animation/index.html) in a browser. It has three tabs:

* **Problem:** the statement and the key idea.
* **Walkthrough:** pick a scenario and press **Play**. Each step is animated and read aloud by your browser's speech
  engine (use the 🔊 *Narration* button to turn the voice on or off; a female voice, Amy when installed, is preferred). Keys: space = play/pause, ← / → = step, 1–9 = scenario.
* **Complexity:** time and space cost, plotted against the common growth curves{", and compared with the other approaches" if others else ""}.

Switch between Light, Medium and Dark themes in the header.
{see_also}"""


def generate_project(p):
    d = ROOT / dir_name(p)
    if d.exists():
        shutil.rmtree(d)
    vs = variants(p)
    for v in vs:
        vd = d / v["dir"]
        src = vd / "src/main/java" / pkg(p, v).replace(".", "/")
        tst = vd / "src/test/java" / pkg(p, v).replace(".", "/")
        bad = FORBIDDEN.search(v["java"])
        assert not bad, f"{p['num']} {v['v']}: uses java.util {bad.group(1)}; use MyHashMap / MyHashSet instead"
        solution = java_file(p, v, v["java"], SOLUTION_IMPORTS)
        write(src / f"{p['cls']}.java", solution)
        hs = helpers_for(v)
        for h in hs:
            write(src / f"{h}.java", java_file(p, v, HELPERS[h], "import java.util.*;\n" if h in ("ListNode", "TreeNode") else ""))
        if "MyHashMap" in hs:
            write(tst / "MyHashMapTest.java", java_file(p, v, HASH_TEST, TEST_IMPORTS))
        write(tst / f"{p['cls']}Test.java", java_file(p, v, v["test"], TEST_IMPORTS))
        write(vd / "build.gradle.kts", BUILD)
        write(vd / "settings.gradle.kts", SETTINGS.replace("__NAME__", f"{dir_name(p)}-{v['dir']}").replace("__JAVA__", str(JAVA)))
        write(vd / ".gitignore", GITIGNORE)
        write(vd / "README.md", variant_readme(p, vs, v))
        write(vd / "animation/index.html", animation_html(p, vs, v, solution))
        shutil.copytree(TOOLS / "wrapper", vd, dirs_exist_ok=True)
        gw = vd / "gradlew"
        gw.chmod(gw.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    write(d / "README.md", problem_readme(p, vs))


def generate_root(probs):
    includes = "\n".join(f'includeBuild("{dir_name(p)}/{v["dir"]}") {{ name = "{dir_name(p)}-{v["dir"]}" }}' for p in probs for v in variants(p))
    write(ROOT / "settings.gradle.kts", f"""// Composite build for convenience only: every solution folder is a standalone Gradle project.
// Including them here lets `./gradlew testAll` (run from gradle-java/) test all of them in one go.
rootProject.name = "leetcode-top-500"

{includes}
""")
    write(ROOT / "build.gradle.kts", """tasks.register("testAll") {
    group = "verification"
    description = "Runs the tests of every standalone solution project."
    dependsOn(gradle.includedBuilds.map { it.task(":test") })
}
""")
    write(ROOT / ".gitignore", GITIGNORE)
    shutil.copytree(TOOLS / "wrapper", ROOT, dirs_exist_ok=True)
    data = []
    for i, p in enumerate(probs, 1):
        data.append({"i": i, "num": p["num"], "title": p["title"], "diff": p["diff"], "topic": p["topic"], "dir": dir_name(p),
                     "versions": [{"v": v["v"], "dir": v["dir"], "name": v["name"], "time": v["cx"]["time"]} for v in variants(p)]})
    page = (TOOLS / "engine" / "index_template.html").read_text()
    page = page.replace("__DATA__", json.dumps(data)).replace("__JAVA__", str(JAVA)).replace("__GRADLE__", GRADLE)
    write(ROOT / "index.html", page)
    rows = []
    for i, p in enumerate(probs, 1):
        d = dir_name(p)
        vs = variants(p)
        links = "<br>".join(f"[{v['dir']}]({d}/{v['dir']}/README.md) · [▶]({d}/{v['dir']}/animation/index.html)" for v in vs)
        rows.append(f"| {i} | {p['num']} | [{p['title']}]({d}/README.md) | {p['diff']} | {p['topic']} | `{vs[-1]['cx']['time']}` | {links} |")
    table = "\n".join(rows)
    write(ROOT / "README.md", f"""# LeetCode Top 500 interview problems — Java {JAVA} + Gradle {GRADLE}

Problems 1–150 follow LeetCode's **Top Interview 150** study plan. Problems 151 onwards are the next most frequently asked
interview classics (LeetCode 75, Blind 75, NeetCode 150, Top 100 Liked and other well-known problems), growing towards 500.
Every solution approach is its own standalone Gradle project:

```
0001-two-sum/
├── README.md                      problem statement and an index of the approaches
├── v1-brute-force/                standalone project: simplest approach
│   ├── README.md                  problem statement + this approach
│   ├── settings.gradle.kts
│   ├── build.gradle.kts
│   ├── gradlew, gradle/wrapper    Gradle {GRADLE} wrapper
│   ├── src/main/java              Java {JAVA} solution
│   ├── src/test/java              JUnit 6 tests
│   └── animation/index.html       narrated, animated walkthrough
└── v2-one-pass-hash-map/          standalone project: the next, more efficient approach (up to v5)
```

Solutions never use `java.util.HashMap` / `HashSet`. Projects that need hashing include `MyHashMap` and `MyHashSet`,
a small hash table written from scratch (bucket array, hash spreading, chaining, resizing), plus their own tests.

Each `animation/index.html` is self-contained and works offline:

* **Problem** tab: statement, examples, key idea and approach.
* **Walkthrough** tab: several scenarios (examples and edge cases) animated step by step; each step is read aloud
  with the browser's Web Speech API (no audio files needed). Hash maps are drawn as real bucket arrays.
* **Complexity** tab: time and space complexity with a growth chart, compared across the problem's approaches.
* Light / Medium / Dark themes (remembered between visits), keyboard shortcuts, and links between approaches.

## Index

Open [`index.html`](index.html) in a browser for a searchable, filterable index that links to every problem, every
approach project and every animation. The table at the end of this file lists the same links.

## Build

```bash
cd 0001-two-sum/v2-one-pass-hash-map && ./gradlew test   # one standalone project
./gradlew testAll                                         # everything (composite build, run from gradle-java/)
```

The Gradle toolchain asks for JDK {JAVA}; the foojay resolver plugin downloads it if it is not installed.

## Regenerating

All projects are generated from `tools/problems/*.py` by `python3 tools/generate.py`.
The shared animation player lives in `tools/engine/`; the hash table in `tools/helpers/`.

## Problems

| # | LeetCode | Problem | Difficulty | Topic | Best time | Approaches |
|---|----------|---------|------------|-------|-----------|------------|
{table}
""")


def main():
    import sys
    if len(sys.argv) > 2 and sys.argv[1] == "--dirs":  # print the project folders of one batch file
        spec = importlib.util.spec_from_file_location("b", TOOLS / "problems" / f"{sys.argv[2]}.py")
        mod = importlib.util.module_from_spec(spec); mod.P = P; spec.loader.exec_module(mod)
        print(" ".join(dir_name(p) for p in mod.PROBLEMS))
        return
    probs = load_problems()
    nums = [p["num"] for p in probs]
    assert len(nums) == len(set(nums)), "duplicate problem numbers"
    for p in probs:
        generate_project(p)
    generate_root(probs)
    print(f"generated {len(probs)} problems, {sum(len(variants(p)) for p in probs)} versions")


if __name__ == "__main__":
    main()
