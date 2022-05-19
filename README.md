# Data Capture App
## Getting Started
### Requirements
- Python 3.+

## Usage
### `DataCapture` class
- `add(item: int)`
  -  Inserts an item to the internal list of items
- `build_stats()` 
  - Builds a `Stats` class exporting different tools for statistics. 
 
### `Stats` class
- `greater(key: int)`
  - Returns how many items are greater than `key`
- `less(key: int)`
  - Returns how many items are lower than `key`
- `between(start: int, end: int)`
  - Returns how many items exit between `start` and `end` (inclusive).

## Example Usage
```python
>>> from data_capture import DataCapture
>>> capture = DataCapture()
>>> capture.add(7)
>>> capture.add(5)
>>> capture.add(3)
>>> capture.add(3)
>>> capture.add(1)
>>> stats = capture.build_stats()
>>> stats.less(3)
1 # Returns 1 since only item 1 is lower than 3
>>> stats.greater(1)
4 # Returns 4 since 3, 3, 5, 7 are greater than 1
>>> stats.between(3, 7)
4 # Returns 4 since 3, 3, 5, 7 exist in the range [3, 7]

```
