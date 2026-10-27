# Temperature feature - leader's contribution

Branch: `feature/temperature`

## Usage

From the repository root:

```bash
python -c "from temperature import celsius_to_fahrenheit; print(celsius_to_fahrenheit(25))"
python -c "from temperature import fahrenheit_to_celsius; print(fahrenheit_to_celsius(77))"
```

Expected results: `77.0` and `25.0`.

## Run tests

```bash
python -m pip install pytest
python -m pytest -v
```

The Celsius formula is `celsius * 9 / 5 + 32`; the inverse is
`(fahrenheit - 32) * 5 / 9`. Inputs must be finite numbers. Booleans,
text, and missing values raise TypeError. Non-finite numbers and values
below absolute zero raise ValueError. The absolute-zero boundary is allowed.
Tests use approximate comparison to accommodate floating-point arithmetic.

## Evidence and review still to collect

- Screenshot of local passing tests and the two feature commits.
- PR link and a teammate's meaningful line comment and approval.
- Review another member's PR yourself and leave a meaningful line comment.
- Coordinate the group's Request changes cycle, controlled README conflict,
  failed/fixed CI, and blocked-PR evidence; these are not completed by this code.

## AI-use notes for the group report

AI assisted with drafting the temperature functions, input validation, tests,
and these notes. The code was checked using pytest. Before submission, the
member must review and understand the implementation and record any changes
they made. The final group paragraph should describe actual use by all members.
