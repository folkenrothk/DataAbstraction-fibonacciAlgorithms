# Fibonacci Algorithms

## Kate Folkenroth

## Program Output

### Experiment Report

*Whenever possible, please use the same "small" and "large" inputs for both the List-based and Tuple-based algorithms.*

*Do not run the program with the `--display` option when conducting experiments!*

*If an algorithm does not work correctly and you can explain why it does not work, then please provide that output in one of the above fenced code blocks.*

This experiment features the comparison of list and tuples as well as the iterative and recursive methods. After running each command four times, below are each of the experiment trials. Each trial has three outputs of the estimated overall memory, estimated peak memory, and estimated execution time according to the simple timer. 

The inputs chosen are paired for the iterative algorithms and then the recursive algorithms. The small input for the iterative functions is 10000 and the large input is 50000. The recursive functions had a small input of 385 and a large input of 985. The recursive has a different set of inputs since there is a limit to how many times a machine do the recursion. The limit is around 1000 for this machine I am working with so I chose the largest integer I could without receiving a stack error. 

As seen below, the simple timer was not precise enough to record the execution time some of the recursive algorithms. Ideally, pyinstrument in the browser should have been run with this experiment but was not functioning properly at the time of this experiment. With future experimentation, timing percision will be an area to improve on. 

In the next section, the outputs displayed in the fenced code blocks are the first runs of each input and algorithm combination. 


**Summary of experiments for the Iterative algorithms**

Summary of the runs for the iterativetuple algorithm:
* Small = `poetry run fibonaccicreator --number 10000 --approach iterativetuple`
    - R1: 33.796875 megabytes, 35.1640625 megabytes, 0.30 seconds
    - R2: 33.79296875 megabytes, 35.06640625 megabytes, 0.29 seconds
    - R3: 33.7890625 megabytes, 35.12109375 megabytes, 0.32 seconds
    - R4: 33.7890625 megabytes, 35.08984375 megabytes, 0.30 seconds

    Average Overall Memory: 33.7919921875 megabytes
    Average Peak Memory: 35.1103515625 megabytes
    Average Execution Time: 0.3025 seconds

* Large = `poetry run fibonaccicreator --number 50000 --approach iterativetuple`
    - R1: 142.0 megabytes, 133.37890625 megabytes, 19.38 seconds
    - R2: 142.0 megabytes, 133.3125 megabytes, 23.98 seconds
    - R3: 142.0 megabytes, 133.3828125 megabytes, 20.34 seconds
    - R4: 142.0 megabytes, 133.328125 megabytes, 26.21 seconds

    Average Overall Memory: 142.0 megabytes
    Average Peak Memory: 133.3505859375 megabytes
    Average Execution Time: 22.4775 seconds

Summary of the  runs for the iterativelist algorithm:
* Small = `poetry run fibonaccicreator --number 10000 --approach iterativelist `
    - R1: 33.515625 megabytes, 35.02734375 megabytes, 0.01 seconds
    - R2: 33.515625 megabytes, 35.19921875 megabytes, 0.01 seconds
    - R3: 33.515625 megabytes, 34.87890625 megabytes, 0.01 seconds
    - R4: 33.515625 megabytes, 35.13671875 megabytes, 0.01 seconds

    Average Overall Memory: 33.515625 megabytes
    Average Peak Memory: 35.060546875 megabytes
    Average Execution Time: 0.01 seconds

* Large = `poetry run fibonaccicreator --number 50000 --approach iterativelist`
    - R1: 141.6484375 megabytes, 132.25 megabytes, 0.10 seconds
    - R2: 141.6484375 megabytes, 132.25 megabytes, 0.10 seconds
    - R3: 141.68359375 megabytes, 132.2734375 megabytes, 0.10 seconds
    - R4: 141.6484375 megabytes, 132.3125 megabytes, 0.11 seconds

    Average Overall Memory: 141.6572265625 megabytes
    Average Peak Memory: 132.271484375 megabytes
    Average Execution Time: 0.41 seconds

**Summary of experiments for the Recursive algorithms**

Summary of the runs for the recursivetuple algorithm:
* Small = `poetry run fibonaccicreator --number 385 --approach recursivetuple`
    - R1: 28.8359375 megabytes, 34.9296875 megabytes, 0.00 seconds
    - R2: 28.84375 megabytes, 35.15234375 megabytes, 0.00 seconds
    - R3: 28.84375 megabytes, 35.1328125 megabytes, 0.00 seconds
    - R4: 28.83984375 megabytes, 35.0625 megabytes, 0.00 seconds

    Average Overall Memory: 28.8408203125 megabytes
    Average Peak Memory: 35.0693358125 megabytes
    Average Execution Time: 0.00 seconds

* Large = `poetry run fibonaccicreator --number 985 --approach recursivetuple`
    - R1: 47.2421875 megabytes, 37.95703125 megabytes, 0.16 seconds
    - R2: 66.5546875 megabytes, 57.03125 megabytes, 0.37 seconds
    - R3: 62.9140625 megabytes, 53.34765625 megabytes, 0.34 seconds
    - R4: 50.3828125 megabytes, 41.00390625 megabytes, 0.22 seconds

    Average Overall Memory: 56.7734375 megabytes
    Average Peak Memory: 47.3349609375 megabytes
    Average Execution Time: 0.2725 seconds

Summary of the runs for the recursivelist algorithm:
* Small = `poetry run fibonaccicreator --number 385 --approach recursivelist`
    - R1: 28.84375 megabytes, 34.97265625 megabytes, 0.00 seconds
    - R2: 28.84375 megabytes, 35.14453125 megabytes, 0.00 seconds
    - R3: 28.84375 megabytes, 35.03515625 megabytes, 0.00 seconds
    - R4: 28.83984375 megabytes, 34.9375 megabytes, 0.00 seconds

    Average Overall Memory: 28.8427734375 megabytes
    Average Peak Memory: 35.0224609375 megabytes
    Average Execution Time: 0.00 seconds

* Large = `poetry run fibonaccicreator --number 985 --approach recursivelist`
    - R1: 29.57421875 megabytes, 35.078125 megabytes, 0.00 seconds
    - R2: 29.33203125 megabytes, 35.22265625 megabytes, 0.00 seconds
    - R3: 29.328125 megabytes, 35.14453125 megabytes, 0.00 seconds
    - R4: 29.828125 megabytes, 35.02734375 megabytes, 0.00 seconds

    Average Overall Memory: 29.515625 megabytes
    Average Peak Memory: 35.1181640625 megabytes
    Average Execution Time: 0.00 seconds

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

From the data collect above, I conclude that the list is faster than the tuple. With both methods (recursive and iterative), the list as the data container was faster. The difference of memory is less than 1 megabyte for both inputs and for peak and overall memory size. Execution times are drastically different between the two. For the small input, the list was 96.7% faster than the tuple and with the large inputs the list was 99.5% faster than the tuple.

Iterative seems faster than recursive. I am unable to draw  Though I was unable to compare directly between the recursive and iterative algorithms, the recursive seemed to be quick. This experiment will need to be conducted with a different machine. This cannot be confirma as the numbers 

The most efficient is the combination of the iteration method and list data container.

One difficulty with recursion, is that their is a limitation (depending on the machine's ability) to the amount of recursion a machine can handle. This is something to consider along with deciding if an algorithm is not suitable.

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

This section of code is the function signature of the function called fibonaccicreator which works with the CLI. This function takes input from the CLI. The inputs are the approach, number, display, and pyinstrument. The approach is a string that needs to match the last part of the function names in the fibonacci.py file. The number is an integer. The approach and number are set as `...` as the default. The display is a boolean set as False unless it takes in `--display` from the keyboard input. The pyinstrument works similarly to display as it is also set as False unless `--pyinstrument` is inputed. 

#### A code segment that calls a function based on its name in a string

```
    # construct the full name of the function to call
    function = FIBONACCI_FUNCTION_BASE + UNDERSCORE + approach
    # construct the requested function from the compute module
    # Reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    function_to_call = getattr(fibonacci, function)
```

This section of code features the part of the fibonaccicreator function that works to call the function. I included the line before it where the string `function` is constructed. This string is made of the global variables `FIBONACCI_FUNCTION_BASE` and `UNDERSCORE` and the input `approach`. This then producees the string of `fibonacci_iterativelist` if the approach input is `iterativelist`. This formats the string to match the functions in the fibonacci.py file. The next line featuring the getattr command. This takes the file name and the string of the function it is looking to call which is then stored in the variable `function_to_call`. This allows us to call functions from another file.

## Professional Development

### What was the greatest challenge that you faced when completing this assignment?

The greatest challenge with this assignment was figuring out how to make it compatible with my Windows machine. I spend a lot of time struggling to understand how docker containers work. I struggling to make it work for my purposes. 

### Leveraging your response to the previous question, how did you overcome the challenge?

I overcame this challenge by doing a couple things. First, I spent time looking through online resources and documentation of how to use a docker container. I then connected with my colleagues to try to resolve the issue. Then, I scheduled office hours to get a fuller understanding and direction of how to conduct the experiment locally through docker. Finally, I just ended up spending time reading documentation and bouncing ideas off of anyone who would listen. I finally found a solution to working with a docker container on my machine though it may only be a work around. After regaining confidence in my code, I distributed this knowledge to my colleagues. 

### Leveraging what you know from all experiments conducted this semester, what are fast ways to perform computations?

From all the experiments we have conducted so far, there are multiple pieces that effect the speed of computations. The fastest data container seems to be the list (at least in comparison to a tuple). This makes sense as lists are mutable and tuple are not. The single-for loop is faster than a double-for loop as seen in the last experiment. This makes sense since the double requires more iterations than a single-for loop. Iterative seems to be faster than recursive process. This makes sense as iterative does not call itself and works through specified range rather than continually calling itself and working towards a base case. Recursion is limited by stack size so when considering the inputs, recursion may not be the right option.


### Leveraging what you know from all experiments conducted this semester, what are slow ways to perform computations?

From the experiments, the pieces that slow the computation contrast those listed in the fast computation paragraph above. The slower data container seems to be the tuple. Tuples are immutable, thus a new one needs to be made each time. The slower for loop is the double-for loop. This requires more iteration. Lastly, the recursive seems to be slower to iterative. The recursive method would be slower since it keeps calling itself and can even run out of room on the AR stack.


