tasks.register("testAll") {
    group = "verification"
    description = "Runs the tests of every standalone solution project."
    dependsOn(gradle.includedBuilds.map { it.task(":test") })
}
