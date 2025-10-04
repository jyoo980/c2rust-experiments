#!/usr/bin/env python

import subprocess

from semver import Version
from subprocess import CompletedProcess, CalledProcessError

CBMC_VERSION = Version.parse("6.5.0")
MINIMUM_RUST_VERSION = Version.parse("1.58.0")
MINIMUM_KANI_VERSION = Version.parse("0.65.0")


def main():
    print(
        f"Checking requirements for:\nCBMC == {CBMC_VERSION}\nRust >= {MINIMUM_RUST_VERSION}\nKani >= {MINIMUM_KANI_VERSION}"
    )
    assert _is_cbmc_installed() and _is_rust_installed() and _is_kani_installed()
    print("Requirements satisfied.")


def _is_cbmc_installed() -> bool:
    get_cbmc_version = "cbmc --version"
    result = _run_cmd(get_cbmc_version)
    installed_cbmc_version = Version.parse(result.stdout.split(" ")[0])
    if installed_cbmc_version.compare(CBMC_VERSION) == 0:
        return True
    raise Exception(
        f"CBMC version {CBMC_VERSION} is required, but found {installed_cbmc_version}"
    )


def _is_rust_installed() -> bool:
    get_rust_version = "rustc --version"
    result = _run_cmd(get_rust_version)
    rust_version_str = result.stdout.split(" ")[1]
    installed_rust_version = Version.parse(rust_version_str)
    if installed_rust_version.compare(MINIMUM_RUST_VERSION) >= 0:
        return True
    raise Exception(
        f"Expected Rust version >={MINIMUM_RUST_VERSION}, but found {installed_rust_version}"
    )


def _is_kani_installed() -> bool:
    get_kani_version = "kani --version"
    result = _run_cmd(get_kani_version)
    kani_version_str = result.stdout.split(" ")[1]
    installed_kani_version = Version.parse(kani_version_str)
    if installed_kani_version.compare(MINIMUM_KANI_VERSION) >= 0:
        return True
    raise Exception(
        f"Expected Kani version >={MINIMUM_RUST_VERSION}, but found {installed_kani_version}"
    )


def _run_cmd(cmd: str) -> CompletedProcess:
    try:
        return subprocess.run(
            args=cmd, shell=True, check=True, capture_output=True, encoding="utf-8"
        )
    except CalledProcessError as e:
        raise Exception(f"Running '{cmd}' raised an error '{str(e)}'")


if __name__ == "__main__":
    main()
