# Nuitka onefile: `__main__.py` package entry point silently exits with code 0

Minimal reproducer for a Nuitka `--onefile` bug where compiling a package's
`__main__.py` directly produces a binary that silently exits 0 with **zero
bytes** on both stdout and stderr.

## Environment

- Nuitka 2.8.10
- Python 3.13
- Ubuntu 24.04 (also reproduced on macOS ARM64)

## Package structure

```
mypkg/
├── __init__.py
├── __main__.py   ← entry point: imports from cli.py, calls hello()
└── cli.py        ← simple Click command
```

`pyproject.toml` declares:

```toml
[project.scripts]
mypkg-cli = "mypkg.__main__:main"
```

## Steps to reproduce

```shell-session
$ uv run python -m mypkg --version
python -m mypkg, version 1.0.0        # ← works

$ uv run nuitka --onefile --assume-yes-for-downloads \
    --output-filename=mypkg.bin mypkg/__main__.py
Nuitka:WARNING: To compile a package with a '__main__' module, specify its
                containing directory …

$ ./mypkg.bin --version
                                       # ← zero output, exit 0

$ ./mypkg.bin --version | wc -c
0
```

## Expected behavior

The binary should print the version string and exit, like the Python invocation.

## Actual behavior

The binary silently exits with code 0 and produces zero bytes on stdout and
stderr. No error, no traceback.

## Workaround

Compile the **package directory** with `--python-flag=-m` instead of the file:

```shell-session
$ uv run nuitka --onefile --assume-yes-for-downloads \
    --python-flag=-m --output-filename=mypkg.bin mypkg/

$ ./mypkg.bin --version
python -m mypkg, version 1.0.0        # ← works
```

## CI workflow

The [GitHub Actions workflow](.github/workflows/build.yaml) demonstrates both
the broken and working approaches side by side.
