# Hongyi-Duan-Rust-2

[![Python CI/CD Pipeline](https://github.com/nogibjj/Hongyi-Duan-Rewrite-Rust-/actions/workflows/PythonCI.yml/badge.svg)](https://github.com/nogibjj/Hongyi-Duan-Rewrite-Rust-/actions/workflows/PythonCI.yml)
[![Rust CI/CD Pipeline](https://github.com/nogibjj/Hongyi-Duan-Rewrite-Rust-/actions/workflows/RustCI.yml/badge.svg)](https://github.com/nogibjj/Hongyi-Duan-Rewrite-Rust-/actions/workflows/RustCI.yml)

To make it clear, I put the performance comparison at first and other parts following.

# Performance Comparison: Python vs Rust

This project compares the performance of statistical functions (mean, median, and standard deviation) implemented in Python and Rust. The goal is to evaluate how much faster Rust is compared to Python when processing large datasets.

## Performance Comparison

The original running results are shown below:

<img width="722" alt="11ca11f8f7d428bdff166c87ce741c2" src="https://github.com/user-attachments/assets/5f76fb9f-14aa-479a-be24-a5423f555eab">
<img width="247" alt="a429683f9144a840b4bd8ce72084b0d" src="https://github.com/user-attachments/assets/75b79d22-c89c-42ab-83c0-2ab94d10a90e">

The following table shows the time taken by each function in both Python and Rust, along with how many times Rust is faster:

| Function             | Python Time (μs) | Rust Time (μs) | Rust Faster Than Python (Times) |
|----------------------|------------------|----------------|---------------------------------|
| Mean                 | 23,539.07        | 4,170          | 5.64                            |
| Median               | 12,088.78        | 7,690          | 1.57                            |
| Standard Deviation    | 125,399.83       | 25,870         | 4.85                            |

## Explanation

- **Mean Calculation**: Rust is about 5.64 times faster than Python for calculating the mean. This can be attributed to Rust's optimized memory handling and the fact that it compiles to native machine code.
  
- **Median Calculation**: Rust is 1.57 times faster than Python for median calculation. The sorting process is likely the bottleneck for both languages, but Rust's sorting algorithm shows moderate performance gains over Python.
  
- **Standard Deviation Calculation**: Rust is 4.85 times faster than Python. As the standard deviation involves both the mean and additional operations (variance calculation and square roots), Rust's performance remains significantly superior.

### Comparison Conclusion

From this comparison, Rust consistently outperforms Python in these statistical calculations, especially when handling large datasets. The most notable speedup is observed in the mean and standard deviation calculations, where Rust is approximately 5 times faster. This makes Rust a strong candidate for high-performance computing tasks that involve heavy numerical operations.

Here’s a detailed `README.md` that you can use for the GitHub project at [Hongyi-Duan-Rewrite-Rust](https://github.com/nogibjj/Hongyi-Duan-Rewrite-Rust-). This README includes an overview, installation instructions, usage guide, as well as a performance comparison between Python and Rust.

## Overview

The goal of this project is to demonstrate the efficiency gains by implementing common statistical functions in Rust versus Python. Rust is known for its speed and memory safety, and this project seeks to quantify how much faster Rust performs these operations on large datasets compared to Python.

## Project Structure

The project consists of the following files:

- **`main.py`**: The Python implementation of the statistical functions.
- **`test_main.py`**: Python test suite that verifies the correctness of the statistical functions.
- **`lib.rs`**: Rust library file that implements the statistical functions (`mean`, `median`, `std`).
- **`main.rs`**: Rust binary file that tests the execution time for the functions implemented in Rust.
- **`Cargo.toml`**: Configuration file for Rust dependencies and metadata.

## Installation

### Python

To run the Python version, you need to install `numpy` for numerical operations and `unittest` for running tests.

1. Clone the repository:

   ```bash
   git clone https://github.com/nogibjj/Hongyi-Duan-Rewrite-Rust-
   cd Hongyi-Duan-Rewrite-Rust-
   ```

2. Install dependencies:

   ```bash
   pip install numpy
   ```

3. Run the Python script:

   ```bash
   python main.py
   ```

### Rust

To run the Rust version, you need to have Rust installed. You can install Rust from the [official website](https://www.rust-lang.org/tools/install).

1. Install Rust (if not already installed):

   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   ```

2. Navigate to the repository directory and build the project:

   ```bash
   cargo build
   ```

3. Run the Rust program:

   ```bash
   cargo run
   ```

## Usage

### Running Python Code

To run the Python version of the project:

```bash
python main.py
```

This will calculate the `mean`, `median`, and `standard deviation` for a large dataset and print the time taken for each operation in microseconds.

### Running Rust Code

To run the Rust implementation:

```bash
cargo run
```

This will perform the same calculations as the Python script and display the time taken by each function.

### Running Tests

#### Python

You can run the Python test suite using:

```bash
python -m unittest discover
```

#### Rust

For the Rust tests, you can run:

```bash
cargo test
```
