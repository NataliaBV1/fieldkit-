# FieldKit 🛠️

**FieldKit** is an open-source Python library and command-line interface (CLI) designed for scientific computing, experimental physics, and engineering calculations.

## Core Features
- **Uncertainty Propagation:** Automatic Gaussian error propagation for physical measurements (x ± δx).
- **Unit Conversion Engine:** Built-in handling for compound physical units.
- **CLI Instrumentation:** Fast, terminal-based engineering calculator.

## Quickstart

### Usage Example
```python
from fieldkit.uncertainty import Measurement

# Define physical measurements (Value ± Uncertainty)
voltage = Measurement(12.0, 0.1)  # 12.0V ± 0.1V
current = Measurement(2.5, 0.05)  # 2.5A ± 0.05A

total = voltage + current
print(f"Result: {total}")

## Testing
Run test suites with `pytest`:
```bash
pytest
