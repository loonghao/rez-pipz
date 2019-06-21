name = "pipz"
version = "1.0.3"
requires = ["python>=2,<4"]

tools = [
    "install",
    "search",
]

build_command = " ".join([
    "python {root}/install.py ",
    "--pip=19.1.1",
    "--wheel=0.33.4",
    "--setuptools=41.0.1",
])


def commands():
    global env

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")