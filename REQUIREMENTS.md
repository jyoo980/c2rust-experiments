# Requirements

You can use the `check_requirements.py` script to validate installation of the requirements
  specified in this document:

```sh
% ./check_requirements.py
```

## CBMC: The C Bounded Model Checker

Install version 6.5.0 of CBMC.
If you are on macOS,
  you can install specific versions from a `homebrew` tap:

```sh
# Install the tap
% brew tap diffblue/cbmc 

# Install cbmc@6.5.0
% brew install diffblue/cbmc/cbmc@6.5.0
```

Confirm a successful installation of CBMC at version 6.5.0:
```sh
% cbmc --version
6.5.0 (cbmc-6.5.0)
```

## Z3: The Z3 Theorem Prover

We use Z3 as the backend solver for CBMC (specified via the `--smt2` flag).

You can install Z3 [from source](https://github.com/Z3Prover/z3),
  via the [instructions in the `README.md`](https://github.com/Z3Prover/z3?tab=readme-ov-file#building-z3-using-make-and-gccclang):

```sh
# Clone the Z3 repository
% git clone git@github.com:Z3Prover/z3.git

# Build Z3
% cd z3/
% python scripts/mk_make.py
% cd build/
% make
```

Running `make` in the `build` repository will take some time,
  but once that is finished,
  you can configure Z3 to be available system-wide:

```sh
# In the same build/ directory
% sudo make install
```

After which you can run Z3 from the command line (re-start your shell if
  necessary).

## Rust and the Kani Verifier

The Kani verifier requires Rust to be installed on your machine.

### Installing Rust

Install Rust 1.58 or newer [via `rustup`](https://rust-lang.org/tools/install/).

Run `rustup --version` and `rustc --version` to confirm they have been installed
  on your machine.

### Installing Kani

Download and build Kani's installer package:

```sh
% cargo install --locked kani-verifier
```

Run the installer:

```sh
% cargo kani setup
```

[Use this command](https://model-checking.github.io/kani/install-guide.html#installing-an-older-version)
  if you require a specific version of Kani.
