# mcp-bb24

A placeholder project for MCP BB24.

## Description

This repository contains the MCP BB24 project files, including a simple command-line number sorting utility.

## Tools

### Number Sorter (`number_sorter.py`)

A Python command-line tool that sorts numbers provided as arguments.

**Usage:**
```bash
python number_sorter.py [options] <numbers...>
```

**Options:**
- `-r, --reverse`: Sort in descending order
- `-i, --integers`: Display results as integers (if all inputs are whole numbers)
- `-h, --help`: Show help message

**Examples:**
```bash
# Basic sorting
python number_sorter.py 5 2 8 1 9
# Output: Sorted numbers: 1 2 5 8 9

# Reverse sorting
python number_sorter.py -r 5 2 8 1 9
# Output: Sorted numbers: 9 8 5 2 1

# Integer output for whole numbers
python number_sorter.py -i 5.0 2.0 8.0 1.0 9.0
# Output: Sorted numbers: 1 2 5 8 9
```

## Getting Started

Documentation and setup instructions will be added as the project develops.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. 