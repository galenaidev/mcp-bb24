#!/usr/bin/env python3
"""
Number Sorter - A simple command-line tool to sort numbers

This script takes numbers as command-line arguments and sorts them in ascending order.
"""

import sys
import argparse


def sort_numbers(numbers):
    """
    Sort a list of numbers in ascending order.
    
    Args:
        numbers (list): List of numbers to sort
        
    Returns:
        list: Sorted list of numbers
    """
    return sorted(numbers)


def parse_arguments():
    """
    Parse command-line arguments.
    
    Returns:
        argparse.Namespace: Parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="Sort numbers provided as command-line arguments",
        epilog="Example: python number_sorter.py 5 2 8 1 9"
    )
    
    parser.add_argument(
        'numbers',
        nargs='+',
        type=float,
        help='Numbers to sort (space-separated)'
    )
    
    parser.add_argument(
        '-r', '--reverse',
        action='store_true',
        help='Sort in descending order'
    )
    
    parser.add_argument(
        '-i', '--integers',
        action='store_true',
        help='Display results as integers (if all inputs are whole numbers)'
    )
    
    return parser.parse_args()


def main():
    """
    Main function that orchestrates the number sorting process.
    """
    try:
        args = parse_arguments()
        
        # Sort the numbers
        sorted_numbers = sort_numbers(args.numbers)
        
        # Reverse if requested
        if args.reverse:
            sorted_numbers.reverse()
        
        # Format output based on options
        if args.integers and all(num.is_integer() for num in sorted_numbers):
            sorted_numbers = [int(num) for num in sorted_numbers]
        
        # Display results
        print("Sorted numbers:", ' '.join(map(str, sorted_numbers)))
        
    except ValueError as e:
        print(f"Error: Invalid number format - {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 