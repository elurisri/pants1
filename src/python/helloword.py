python_distribution(
  name="helloworld-dist",
  description=env("DIST_DESC", "Set the `DIST_DESC` env variable to override this value."),
  provides=python_artifact(
    name="helloworld",
    version=env("HELLO_WORLD_VERSION"),
  ),
)
