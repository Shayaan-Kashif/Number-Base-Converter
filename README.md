# Number Base Converter

This program effortlessly converts Decimal, Binary and Hexadecimal numbers.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)


## Installation

To clone and run this application, follow the instructions below:

1. Clone the repository:

    ```bash
    git clone https://github.com/Shayaan-Kashif/Number-Base-Converter.git
    ```

2. Navigate into the cloned repository directory:

    ```bash
    cd Number-Base-Converter
    ```



## Usage

### Usage Case: Number Base Converter

#### Scenario:

**User:** A software developer working on a project that involves low-level memory management and requires frequent conversions between different number systems (binary, decimal, hexadecimal).

#### Objective:

The developer wants to convert numbers between different numeral systems (hexadecimal, decimal, binary) efficiently without manually calculating the conversions.

#### Steps:

1. **Input:**
   - The developer inputs a number in one of the supported formats (binary, decimal, or hexadecimal).
   - The program detects the format of the input (e.g., `0b101010` for binary, `0x2A` for hexadecimal, or `42` for decimal).

2. **Action:**
   - The program automatically converts the input number to the other two formats. For example, if the developer inputs `0x2A` (hexadecimal), the program converts it to its decimal (`42`) and binary (`0b101010`) equivalents.

3. **Output:**
   - The converted values are displayed clearly, showing the original input and the converted results in all three formats.

4. **Example:**

   - **Input:** `0x2A` (Hexadecimal)
   - **Output:**
     - Decimal: `42`
     - Binary: `0b101010`

5. **User Benefit:**
   - The developer quickly obtains accurate conversions without manually working through the math, which reduces errors and saves time, especially when debugging or writing code involving low-level data operations.

#### Additional Features:
- The program can also support negative numbers and floating-point numbers if needed.
- The developer can choose to copy any of the converted values to their clipboard for use in their project.

## Features

- Converts numbers between hexadecimal, decimal, and binary formats.
- User-friendly interface for seamless conversion.
- Additional options for floating-point and negative number conversion.
