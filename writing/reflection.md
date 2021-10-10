# Fibonacci Algorithms

## Kate Folkenroth

## Program Output

### Use eight fenced code blocks to provide output from eight different runs of `fibonaccicreator` with different inputs

TODO: Provide the output for running `iterativetuple` with a large and small input
TODO: Use a fenced code block to provide the requested output

TODO: Provide the output for running `iterativelist` with a large and small input
TODO: Use a fenced code block to provide the requested output

TODO: Provide the output for running `recursivetuple` with a large and small input
TODO: Use a fenced code block to provide the requested output

TODO: Provide the output for running `recursivelist` with a large and small input
TODO: Use a fenced code block to provide the requested output

TODO: If an algorithm does not work correctly and you can explain why it does not
work, then please provide that output in one of the above fenced code blocks

TODO: Whenever possible, please use the same "small" and "large" inputs for both
the List-based and Tuple-based algorithms.

TODO: Use the `--pyinstrument` command-line argument to open up a web-based display
of the call profile from running your program. You can use this output to understand
the other profiling information that `fibonaccicreator` can produce.

TODO: Do not run the program with the `--display` option when conducting
experiments!

TODO: Document and justify your choice for the `number` parameter.

#### Two outputs from running the `iterativetuple`

TODO: Provide a fenced code block with the requested outputs

#### Two outputs from running the `iterativelist`

TODO: Provide a fenced code block with the requested outputs

#### Two outputs from running the `recursivetuple`

TODO: Provide a fenced code block with the requested outputs

#### Two outputs from running the `recursivelist`

TODO: Provide a fenced code block with the requested outputs

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
