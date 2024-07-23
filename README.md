# CreateDirectory

The `CreateDirectory` class is a Python utility for creating directories. It allows you to create a single directory or multiple directories, wither from a single string or a list of strings. The class includes a validation for the directory and logs.

## Features

- Create a single directory or multiple directories.
- Validate the directory path.
- Handle directory names with or without spaces.
- Log operations for better traceabillity.

## Requirements

- Python 3.x
- `logging` (standard library)

## Installation

You can install `CreateDirectory` directly from GitHub using `pip`.

```sh
pip install git+https://github.com/fernandoluiz2003/CreateDirectory.git
```

## Usage

### Basic Usage

```python
from create_directory import CreateDirectory

# Create a single directory
create_dir = CreateDirectory(
    folder_name="my_directory",
    dir_path "/path/to/directory"
)
print(create_dir.get_new_path())

# Create a multiple directory
create_dirs = CreateDirectory(
    folder_name=["dir1", "dir2"],
    dir_path "/path/to/directory"
)
print(create_dirs.get_new_path())
```