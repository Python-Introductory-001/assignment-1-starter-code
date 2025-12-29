# Assignment 1 — Introductory Python

Welcome to Assignment 1. This repository contains two small, beginner-friendly programming problems designed to help you get comfortable reading and editing Python code, running tests, and using basic operators and functions.

**Project Layout**

- `P1/` — Problem 1 source code. See `P1/helloworld.py`.
- `P2/` — Problem 2 source code. See `P2/calculator.py`.
- `tests/` — Automated tests you can run locally (uses `pytest`).

**Getting Started**

1. Make sure you have Python 3 installed (Python 3.8+ recommended).
2. (Optional) Install `pytest` for running the tests:

	 ```bash
	 python3 -m pip install --user pytest
	 ```

3. Edit the source files in the `P1/` and `P2/` folders using your editor.

**Problem 1 — P1**

- Goal: Learn the structure of a basic Python program and return a greeting string.
- Where to work: edit the function `greet()` in `P1/helloworld.py`.
- What the tests check: the function returns a string of the expected greeting and the return type is `str`.
- Notes: Keep the implementation simple and make sure the function returns the required value.

**Problem 2 — P2**

- Goal: Practice using variables, operators, and simple functions by implementing basic calculator operations.
- Where to work: implement the functions in `P2/calculator.py` — `add`, `subtract`, `multiply`, `divide`, and the `calculator` dispatcher.
- What the tests check: each operation returns the correct numeric result and the dispatcher uses the correct operation based on its inputs.
- Notes: Do not change the function names or signatures — the tests import and call them directly.
 - Calculator arguments: the `calculator(num1, num2, operator, resultType)` function will be called with the following values:
	 - `num1`, `num2`: the numeric operands.
	 - `operator`: a string indicating the operation — one of `'+'`, `'-'`, `'*'`, `'/'`.
	 - `resultType`: a string indicating the desired return type — `'f'` for float or `'i'` for integer.
 	 - Behavior: when `resultType` is `'f'` the returned value should be a float; when `resultType` is `'i'` the returned value should be an integer.
 	 - Division errors: if a division operation is invalid (for example dividing by zero) the function should return the string "ERROR!" instead of raising an exception.

**Running the Tests**

- Run a single problem's tests (example for P1):

	```bash
	pytest tests/P1.py -q
	```

- Run all tests in the repository:

	```bash
	pytest -q
	```

**Problem 3 — P3**

- Goal: Analyze enzyme activity measurements and classify them as `low`, `normal`, or `high` and compute simple summary statistics.
- Where to work: edit `P3/enzymes-analyzer.py`.
- Key functions:
  - `classify_activity(activity_value)` — returns `'low'`, `'normal'`, or `'high'` according to the ranges:
    - below 40: `low`
    - 40–70 (inclusive): `normal`
    - above 70: `high`
  - `analyze_activities(activity_list)` — returns a dictionary with keys: `low_count`, `normal_count`, `high_count`, `average_activity`, `min_activity`, `max_activity`, and `normal_values` (a list of values classified as normal in input order).
  - `print_summary(results, total_samples)` — prints a human-readable summary of the results.
- What the tests check: boundary classifications (40 and 70 inclusive), correct counts, correct average/min/max calculations, preservation of `normal_values` order, and formatted summary output.

**Running P3 tests**

- Run only P3 tests:

	```bash
	pytest tests/P3.py -q
	```


If you do not have `pytest` installed, you can still run Python files directly while developing, but the test commands above are the recommended check before submitting.

**Submission & Tips**

- Keep changes limited to the files inside `P1/` and `P2/` unless instructed otherwise.
- Run tests frequently as you make small changes.
- Follow consistent naming and simple, readable code — this helps when debugging and when your instructors review your work.