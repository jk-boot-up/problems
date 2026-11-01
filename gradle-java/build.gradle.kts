tasks.register("testAll") {
    group = "verification"
    description = "Runs the tests of every solution version of every included problem."
    dependsOn(gradle.includedBuilds.map { it.task(":test") })
}
