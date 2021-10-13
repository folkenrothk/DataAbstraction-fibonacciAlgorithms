# Fibonacci Algorithms

## Kate Folkenroth

## Program Output

### Experiment Report

*Whenever possible, please use the same "small" and "large" inputs for both the List-based and Tuple-based algorithms.*

*Do not run the program with the `--display` option when conducting experiments!*

*If an algorithm does not work correctly and you can explain why it does not work, then please provide that output in one of the above fenced code blocks.*

//TODO// Preface: how many runs, the two types of data, inputs and why, sections not working.

**Summary of experiments for the Iterative algorithms**

Summary of the runs for the iterativetuple algorithm:
* Small = `poetry run fibonaccicreator --number 10000 --approach iterativetuple`
    - R1: 33.796875 megabytes, 35.1640625 megabytes, 0.30 seconds
    - R2: 33.79296875 megabytes, 35.06640625 megabytes, 0.29 seconds
    - R3: 33.7890625 megabytes, 35.12109375 megabytes, 0.32 seconds
    - R4: 33.7890625 megabytes, 35.08984375 megabytes, 0.30 seconds
    Average Overall Memory:
    Average Peak Memory:
    Average Execution Time:
* Large = `poetry run fibonaccicreator --number 50000 --approach iterativetuple`
    - R1: 142.0 megabytes, 133.37890625 megabytes, 19.38 seconds
    - R2: 142.0 megabytes, 133.3125 megabytes, 23.98 seconds
    - R3: 142.0 megabytes, 133.3828125 megabytes, 20.34 seconds
    - R4: 142.0 megabytes, 133.328125 megabytes, 26.21 seconds
    Average Overall Memory:
    Average Peak Memory:
    Average Execution Time:
Summary of the  runs for the iterativelist algorithm:
* Small = `poetry run fibonaccicreator --number 10000 --approach iterativelist `
    - R1: 33.515625 megabytes, 35.02734375 megabytes, 0.01 seconds
    - R2: 33.515625 megabytes, 35.19921875 megabytes, 0.01 seconds
    - R3: 33.515625 megabytes, 34.87890625 megabytes, 0.01 seconds
    - R4: 33.515625 megabytes, 35.13671875 megabytes, 0.01 seconds
    Average Overall Memory: 33.515625 megabytes
    Average Peak Memory: 
    Average Execution Time: 0.01 seconds
* Large = `poetry run fibonaccicreator --number 50000 --approach iterativelist`
    - R1: 141.6484375 megabytes, 132.25 megabytes, 0.10 seconds
    - R2: 141.6484375 megabytes, 132.25 megabytes, 0.10 seconds
    - R3: 141.68359375 megabytes, 132.2734375 megabytes, 0.10 seconds
    - R4: 141.6484375 megabytes, 132.3125 megabytes, 0.11 seconds
    Average Overall Memory:
    Average Peak Memory:
    Average Execution Time:

**Summary of experiments for the Recursive algorithms**

Summary of the runs for the recursivetuple algorithm:
* Small = `poetry run fibonaccicreator --number 385 --approach recursivetuple`
    - R1: 28.8359375 megabytes, 34.9296875 megabytes, 0.00 seconds
    - R2: 28.84375 megabytes, 35.15234375 megabytes, 0.00 seconds
    - R3: 28.84375 megabytes, 35.1328125 megabytes, 0.00 seconds
    - R4: 28.83984375 megabytes, 35.0625 megabytes, 0.00 seconds
    Average Overall Memory:
    Average Peak Memory:
    Average Execution Time:
* Large = `poetry run fibonaccicreator --number 985 --approach recursivetuple`
    - R1: 47.2421875 megabytes, 37.95703125 megabytes, 0.16 seconds
    - R2: 66.5546875 megabytes, 57.03125 megabytes, 0.37 seconds
    - R3: 62.9140625 megabytes, 53.34765625 megabytes, 0.34 seconds
    - R4: 50.3828125 megabytes, 41.00390625 megabytes, 0.22 seconds
    Average Overall Memory:
    Average Peak Memory:
    Average Execution Time:
Summary of the runs for the recursivelist algorithm:
* Small = `poetry run fibonaccicreator --number 385 --approach recursivelist`
    - R1: 28.84375 megabytes, 34.97265625 megabytes, 0.00 seconds
    - R2: 28.84375 megabytes, 35.14453125 megabytes, 0.00 seconds
    - R3: 28.84375 megabytes, 35.03515625 megabytes, 0.00 seconds
    - R4: 28.83984375 megabytes, 34.9375 megabytes, 0.00 seconds
    Average Overall Memory:
    Average Peak Memory:
    Average Execution Time:
* Large = `poetry run fibonaccicreator --number 985 --approach recursivelist`
    - R1: 29.57421875 megabytes, 35.078125 megabytes, 0.00 seconds
    - R2: 29.33203125 megabytes, 35.22265625 megabytes, 0.00 seconds
    - R3: 29.328125 megabytes, 35.14453125 megabytes, 0.00 seconds
    - R4: 29.828125 megabytes, 35.02734375 megabytes, 0.00 seconds
    Average Overall Memory:
    Average Peak Memory:
    Average Execution Time:

### Use eight fenced code blocks to provide output from eight different runs of `fibonaccicreator` with different inputs

#### Two outputs from running the `iterativetuple`

The iterativetuple with a small input:
    `poetry run fibonaccicreator --number 10000 --approach iterativetuple`

```
🧳 Awesome, the chosen type of approach is the iterativetuple!

🧮 The program will compute up to the 10000th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   33.796875 megabytes

Estimated peak memory according to the operating system:
   35.1640625 megabytes

Estimated execution time according to the simple timer:
    0.30 seconds
```

The iterativetuple with a large output:
    `poetry run fibonaccicreator --number 50000 --approach iterativetuple`

```
🧳 Awesome, the chosen type of approach is the iterativetuple!

🧮 The program will compute up to the 50000th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   142.0 megabytes

Estimated peak memory according to the operating system:
   133.37890625 megabytes

Estimated execution time according to the simple timer:
    19.38 seconds
```

#### Two outputs from running the `iterativelist`

The iterativelist with a small input:
    `poetry run fibonaccicreator --number 10000 --approach iterativelist`

```
🧳 Awesome, the chosen type of approach is the iterativelist!

🧮 The program will compute up to the 10000th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   33.515625 megabytes

Estimated peak memory according to the operating system:
   35.02734375 megabytes

Estimated execution time according to the simple timer:
    0.01 seconds
```
The iterativelist with a large output:
    `poetry run fibonaccicreator --number 50000 --approach iterativelist`

```
🧳 Awesome, the chosen type of approach is the iterativelist!

🧮 The program will compute up to the 50000th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   141.6484375 megabytes

Estimated peak memory according to the operating system:
   132.25 megabytes

Estimated execution time according to the simple timer:
    0.10 seconds
```

#### Two outputs from running the `recursivetuple`

The recursivetuple with a small input:
    `poetry run fibonaccicreator --number 385 --approach recursivetuple`

```
🧳 Awesome, the chosen type of approach is the recursivetuple!

🧮 The program will compute up to the 385th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   28.8359375 megabytes

Estimated peak memory according to the operating system:
   34.9296875 megabytes

Estimated execution time according to the simple timer:
    0.00 seconds
```

The recursivetuple with a large input:
    `poetry run fibonaccicreator --number 985 --approach recursivetuple`

```
🧳 Awesome, the chosen type of approach is the recursivetuple!

🧮 The program will compute up to the 985th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   47.2421875 megabytes

Estimated peak memory according to the operating system:
   37.95703125 megabytes

Estimated execution time according to the simple timer:
    0.16 seconds
```

#### Two outputs from running the `recursivelist`

The recursivelist with a small input:
    `poetry run fibonaccicreator --number 385 --approach recursivelist`

```
🧳 Awesome, the chosen type of approach is the recursivelist!

🧮 The program will compute up to the 385th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   28.84375 megabytes

Estimated peak memory according to the operating system:
   34.97265625 megabytes

Estimated execution time according to the simple timer:
    0.00 seconds
```
The recursivelist with a large input:
    `poetry run fibonaccicreator --number 985 --approach recursivelist`

```
🧳 Awesome, the chosen type of approach is the recursivelist!

🧮 The program will compute up to the 985th Fibonacci number!

🤷 So, was this an efficient approach for storing the Fibonacci sequence?

Estimated overall memory according to the operating system:
   29.57421875 megabytes

Estimated peak memory according to the operating system:
   35.078125 megabytes

Estimated execution time according to the simple timer:
    0.00 seconds
```

## Performance Analysis

TODO: Provide five paragraphs that explain which algorithm is fastest, by how
much it is faster, and how you knew that it was faster, referencing the data
in the aforementioned command outputs to support your response. You should make
sure that you answer the following research questions:

- RQ: Is `fibonaccicreator` faster with a list or a tuple?
- RQ: Is `fibonaccicreator` faster with recursion or iteration?
- RQ: Overall, what is the fastest approach when using `fibonaccicreator`?
- RQ: Overall, what is the most memory efficient approach when using `fibonaccicreator`?
- RQ: Overall, what are inappropriate approaches for computing Fibonacci numbers?

TODO: Make sure that your responses explain WHY certain algorithms are faster!
TODO: It is not sufficient to only explain WHICH algorithm is faster!
TODO: Make sure that your responses explain WHY certain algorithms use less memory!
TODO: It is not sufficient to only explain WHICH algorithm algorithm uses less memory!
TODO: Make sure that you explain why certain algorithms are not suitable!

## Source Code

### Describe in detail how the completed source code works

#### A function signature that defines the command-line interface for `fibonaccicreator`

```
@cli.command()
def fibonaccicreator(
    approach: str = typer.Option(...),
    number: int = typer.Option(...),
    display: bool = typer.Option(False, "--display"),
    pyinstrument: bool = typer.Option(False, "--pyinstrument"),
):
```
TODO: Write at least one paragraph to explain the request source code
TODO: Explain each of the command-line arguments for this program

#### A code segment that calls a function based on its name in a string

```
    # construct the full name of the function to call
    function = FIBONACCI_FUNCTION_BASE + UNDERSCORE + approach
    # construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    function_to_call = getattr(fibonacci, function)
    # call the constructed function and capture the result
```
TODO: Write at least one paragraph to explain the request source code
TODO: Explain exactly how Python can call a function using a string

## Professional Development

### What was the greatest challenge that you faced when completing this assignment?

The greatest challenge with this assignment was figuring out how to make it compatible with my Windows machine.  // TODO //

### Leveraging your response to the previous question, how did you overcome the challenge?

I overcame this challenge by doing a couple things. First, I spent time looking through online resources and documentation of how to use a docker container. I then connected with my colleagues to try to resolve the issue. Finally, I scheduled office hours to get a fuller understanding and direction of how to conduct the experiment locally through docker. After regaining confidence in my code, I distributed this knowledge to my colleagues. 

### Leveraging what you know from all experiments conducted this semester, what are fast ways to perform computations?

TODO: Provide a one-paragraph response that answers this question in your own words. //List, single for loop, recursive or iterative? //

### Leveraging what you know from all experiments conducted this semester, what are slow ways to perform computations?

TODO: Provide a one-paragraph response that answers this question in your own words. // Tuple, double-for-loops, recursive or iterative //
