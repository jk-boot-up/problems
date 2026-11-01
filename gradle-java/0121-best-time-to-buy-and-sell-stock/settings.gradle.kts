plugins {
    // Downloads JDK 25 automatically if it is not installed locally.
    id("org.gradle.toolchains.foojay-resolver-convention") version "1.0.0"
}

rootProject.name = "0121-best-time-to-buy-and-sell-stock"

// Each solution variant (v1 = simplest ... vN = most efficient) is its own subproject.
include("v1")
include("v2")
