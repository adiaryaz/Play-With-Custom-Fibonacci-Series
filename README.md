# Play With Custom Fibonacci Series

A program to generate a custom Fibonacci series based on user-defined base values and length.

## 📝 Description

This program takes two starting numbers (`base1`, `base2`) and a length (`n`), then generates a sequence where each new number is the sum of the preceding two.

The key difference from a standard Fibonacci problem is that `n` represents the number of elements to generate *after* the initial two base numbers. Therefore, the total length of the final series will be `n + 2`.

-----

## 🎯 Problem Statement

### Input:

  * The first input is a positive integer (`n`), representing the number of elements to generate *after* the base values.
  * The second input is the first base value (`base1`).
  * The third input is the second base value (`base2`).

### Output:

  * A string of space-separated numbers representing the custom Fibonacci series.
  * "NotProceed" if the inputs are invalid.

### Rules:

1.  The input **n** must be a **positive integer** (greater than 0).
2.  The second base value (`base2`) **cannot be lower** than the first base value (`base1`).
3.  If `n` is zero or negative, or if `base2 < base1`, the program should output the message **"NotProceed"**.
4.  The series starts with `base1` and `base2`.
5.  The total length of the printed series will be `n + 2`.

-----

## 💡 Examples

### Example 1 (n = 5, base1 = 2, base2 = 2)

**Input:**

```
5
2
2
```

**Output:**

```
2 2 4 6 10 16 26
```

**Explanation:** The series starts with `2 2`. It then generates `n=5` more numbers:
(2+2=**4**), (2+4=**6**), (4+6=**10**), (6+10=**16**), (10+16=**26**).
The total length is 7 (which is n+2).

### Example 2 (n = 3, base1 = 1, base2 = 2)

**Input:**

```
3
1
2
```

**Output:**

```
1 2 3 5 8
```

**Explanation:** The series starts with `1 2`. It then generates `n=3` more numbers:
(1+2=**3**), (2+3=**5**), (3+5=**8**).
The total length is 5 (which is n+2).

### Example 3 (n = 4, base1 = 3, base2 = 2)

**Input:**

```
4
3
2
```

**Output:**

```
NotProceed
```

**Explanation:** The second base (`base2=2`) is lower than the first base (`base1=3`).

### Example 4 (n = -5)

**Input:**

```
-5
```

**Output:**

```
NotProceed
```

**Explanation:** The length `n` is negative, which is not a positive integer.

### Example 5 (n = 0)

**Input:**

```
0
```

**Output:**

```
NotProceed
```

**Explanation:** The length `n` is 0, which is not a positive integer.

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/custom-fibonacci-series.git
    cd custom-fibonacci-series
    ```

2.  **Run the program** (assuming the file is `main.py`):

    ```bash
    python main.py
    ```

    Enter `n`, `base1`, and `base2` on separate lines when prompted to see the result.
