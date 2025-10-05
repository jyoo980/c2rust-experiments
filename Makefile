default: style-fix style-check type-check

style-fix: python-style-fix
style-check: python-style-check
type-check: python-type-check

PYTHON_FILES:=$(shell find . -type f -name '*.py' -not -path "./.venv/*")
python-style-fix:
	@ruff --version
	@ruff format ${PYTHON_FILES}
	@ruff -q check ${PYTHON_FILES} --fix
python-style-check:
	@ruff --version
	@ruff -q format --check ${PYTHON_FILES}
	@ruff -q check ${PYTHON_FILES}
python-type-check:
	@mypy --strict ${PYTHON_FILES} > /dev/null 2>&1 || true
	@mypy --strict --disallow-any-unimported --namespace-packages --explicit-package-bases ${PYTHON_FILES}

showvars:
	echo "PYTHON_FILES=${PYTHON_FILES}"