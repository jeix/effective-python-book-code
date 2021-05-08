# effective-python-book-code

![Effecive Python 2nd](https://image.aladin.co.kr/product/25432/17/cover150/k552633414_1.jpg)

# Effective Python 2/e

## 1. Pythonic Thinking

#### 01 Know Which Version of Python You’re Using

#### 02 Follow the PEP 8 Style Guide

#### 03 Know the Differences Between `bytes` and `str`

#### 04 Prefer Interpolated F-Strings Over C-style Format Strings and `str.format`

#### 05 Write Helper Functions Instead of Complex Expressions

#### 06 Prefer Multiple Assignment Unpacking Over Indexing

#### 07 Prefer `enumerate` Over `range`

#### 08 Use `zip` to Process Iterators in Parallel

#### 09 Avoid `else` Blocks After `for` and `while` Loops

#### 10 Prevent Repetition with Assignment Expressions

## 2. Lists and Dictionaries

#### 11 Know How to Slice Sequences

#### 12 Avoid Striding and Slicing in a Single Expression

#### 13 Prefer Catch-All Unpacking Over Slicing

#### 14 Sort by Complex Criteria Using the `key` Parameter

#### 15 Be Cautious When Relying on `dict` Insertion Ordering

#### 16 Prefer `get` Over `in` and `KeyError` to Handle Missing Dictionary Keys

#### 17 Prefer `defaultdict` Over `setdefault` to Handle Missing Items in Internal State

#### 18 Know How to Construct Key-Dependent Default Values with `__missing__`

## 3. Functions

#### 19 Never Unpack More Than Three Variables When Functions Return Multiple Values

#### 20 Prefer Raising Exceptions to Returning `None`

#### 21 Know How Closures Interact with Variable Scope

#### 22 Reduce Visual Noise with Variable Positional Arguments

#### 23 Provide Optional Behavior with Keyword Arguments

#### 24 Use `None` and Docstrings to Specify Dynamic Default Arguments

#### 25 Enforce Clarity with Keyword-Only and Position-Only Arguments

#### 26 Define Function Decorators with `functools.wraps`

## 4. Comprehensions and Generators

#### 27 Use Comprehensions Instead of `map` and `filter`

#### 28 Avoid More Than Two Control Subexpressions in Comprehensions

#### 29 Avoid Repeated Work in Comprehensions by Using Assignment Expressions

#### 30 Consider Generators Instead of Returning Lists

#### 31 Be Defensive When Iterating Over Arguments

#### 32 Consider Generator Expressions for Large List Comprehensions

#### 33 Compose Multiple Generators with `yield from`

#### 34 Avoid Injecting Data into Generators with `send`

#### 35 Avoid Causing State Transitions in Generators with `throw`

#### 36 Consider `itertools` for Working with Iterators and Generators

## 5. Classes and Interfaces

#### 37 Compose Classes Instead of Nesting Many Levels of Built-in Types

#### 38 Accept Functions Instead of Classes for Simple Interfaces

#### 39 Use `@classmethod` Polymorphism to Construct Objects Generically

#### 40 Initialize Parent Classes with `super`

#### 41 Consider Composing Functionality with Mix-in Classes

#### 42 Prefer Public Attributes Over Private Ones

#### 43 Inherit from `collections.abc` for Custom Container Types

## 6. Metaclasses and Attributes

#### 44 Use Plain Attributes Instead of Setter and Getter Methods

#### 45 Consider `@property` Instead of Refactoring Attributes

#### 46 Use Descriptors for Reusable `@property` Methods

#### 47 Use `__getattr__`, `__getattribute__`, and `__setattr__` for Lazy Attributes

#### 48 Validate Subclasses with `__init_subclass__`

#### 49 Register Class Existence with `__init_subclass__`

#### 50 Annotate Class Attributes with `__set_name__`

#### 51 Prefer Class Decorators Over Metaclasses for Composable Class Extensions

## 7. Concurrency and Parallelism

#### 52 Use `subprocess` to Manage Child Processes

#### 53 Use Threads for Blocking I/O, Avoid for Parallelism

#### 54 Use `Lock` to Prevent Data Races in Threads

#### 55 Use `Queue` to Coordinate Work Between Threads

#### 56 Know How to Recognize When Concurrency Is Necessary

#### 57 Avoid Creating New `Thread` Instances for On-demand Fan-out

#### 58 Understand How Using `Queue` for Concurrency Requires Refactoring

#### 59 Consider `ThreadPoolExecutor` When Threads Are Necessary for Concurrency

#### 60 Achieve Highly Concurrent I/O with Coroutines

#### 61 Know How to Port Threaded I/O to `asyncio`

#### 62 Mix Threads and Coroutines to Ease the Transition to `asyncio`

#### 63 Avoid Blocking the `asyncio` Event Loop to Maximize Responsiveness

#### 64 Consider `concurrent.futures` for True Parallelism

## 8. Robustness and Performance

#### 65 Take Advantage of Each Block in `try`/`except`/`else`/`finally`

#### 66 Consider `contextlib` and `with` Statements for Reusable `try`/`finally` Behavior

#### 67 Use `datetime` Instead of `time` for Local Clocks

#### 68 Make `pickle` Reliable with `copyreg`

#### 69 Use `decimal` When Precision Is Paramount

#### 70 Profile Before Optimizing

#### 71 Prefer `deque` for Producer–Consumer Queues

#### 72 Consider Searching Sorted Sequences with `bisect`

#### 73 Know How to Use `heapq` for Priority Queues

#### 74 Consider `memoryview` and `bytearray` for Zero-Copy Interactions with bytes

## 9. Testing and Debugging

#### 75 Use `repr` Strings for Debugging Output

#### 76 Verify Related Behaviors in `TestCase` Subclasses

#### 77 Isolate Tests from Each Other with `setUp`, `tearDown`, `setUpModule`, and `tearDownModule`

#### 78 Use Mocks to Test Code with Complex Dependencies

#### 79 Encapsulate Dependencies to Facilitate Mocking and Testing

#### 80 Consider Interactive Debugging with `pdb`

#### 81 Use `tracemalloc` to Understand Memory Usage and Leaks

## 10. Collaboration

#### 82 Know Where to Find Community-Built Modules

#### 83 Use Virtual Environments for Isolated and Reproducible Dependencies

#### 84 Write Docstrings for Every Function, Class, and Module

#### 85 Use Packages to Organize Modules and Provide Stable APIs

#### 86 Consider Module-Scoped Code to Configure Deployment Environments

#### 87 Define a Root `Exception` to Insulate Callers from APIs

#### 88 Know How to Break Circular Dependencies

#### 89 Consider `warnings` to Refactor and Migrate Usage

#### 90 Consider Static Analysis via `typing` to Obviate Bugs

:wq