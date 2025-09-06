## PASSED, feels weird just using time.sleep so I am making is async as well, documentation is very important

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import unittest
import time
import asyncio

async def problem_async(n, f, **params):
    await asyncio.sleep(n/1000)
    return f(**params)

def problem(n, f, **params):
    time.sleep(n/1000)
    return f(**params)

class TestJobSchedulerSync(unittest.TestCase):
    def test_calls_function_after_delay(self):
        called = {"t": None}
        delay_ms = 50
        start = time.monotonic()

        def f():
            called["t"] = time.monotonic()

        problem(delay_ms, f)
        self.assertIsNotNone(called["t"])
        elapsed_ms = (called["t"] - start) * 1000.0
        self.assertGreaterEqual(elapsed_ms, delay_ms - 5)

    def test_zero_delay(self):
        called = {"t": None}
        start = time.monotonic()

        def f():
            called["t"] = time.monotonic()

        problem(0, f)
        self.assertIsNotNone(called["t"])
        elapsed_ms = (called["t"] - start) * 1000.0
        self.assertLess(elapsed_ms, 20.0)

    def test_passes_kwargs(self):
        received = {}
        def f(a=None, b=None):
            received["a"] = a
            received["b"] = b
            return (a, b)

        result = problem(10, f, a=123, b="xyz")
        self.assertEqual(received, {"a": 123, "b": "xyz"})
        self.assertEqual(result, (123, "xyz"))

    def test_returns_function_result(self):
        def f(x): return x * 2
        out = problem(10, f, x=7)
        self.assertEqual(out, 14)

    def test_function_raises_is_propagated(self):
        def f(): raise ValueError("boom")
        with self.assertRaises(ValueError):
            problem(5, f)

    def test_multiple_schedules_sequential(self):
        times = []
        def f(): times.append(time.monotonic())

        start = time.monotonic()
        problem(20, f)
        problem(30, f)

        self.assertEqual(len(times), 2)
        first_ms = (times[0] - start) * 1000.0
        second_ms = (times[1] - start) * 1000.0
        self.assertGreaterEqual(first_ms, 15.0)
        self.assertGreaterEqual(second_ms, 45.0)

class TestJobSchedulerAsync(unittest.IsolatedAsyncioTestCase):
    async def test_calls_function_after_delay(self):
        called = {"t": None}
        delay_ms = 50
        start = time.monotonic()

        def f():
            called["t"] = time.monotonic()

        await problem_async(delay_ms, f)   # await, no asyncio.run
        self.assertIsNotNone(called["t"])
        elapsed_ms = (called["t"] - start) * 1000.0
        self.assertGreaterEqual(elapsed_ms, delay_ms - 5)

    async def test_zero_delay(self):
        called = {"t": None}
        start = time.monotonic()

        def f():
            called["t"] = time.monotonic()

        await problem_async(0, f)
        self.assertIsNotNone(called["t"])
        elapsed_ms = (called["t"] - start) * 1000.0
        self.assertLess(elapsed_ms, 20.0)

    async def test_passes_kwargs(self):
        received = {}
        def f(a=None, b=None):
            received["a"] = a
            received["b"] = b
            return (a, b)

        result = await problem_async(10, f, a=123, b="xyz")
        self.assertEqual(received, {"a": 123, "b": "xyz"})
        self.assertEqual(result, (123, "xyz"))

    async def test_returns_function_result(self):
        def f(x): return x * 2
        out = await problem_async(10, f, x=7)
        self.assertEqual(out, 14)

    async def test_function_raises_is_propagated(self):
        def f(): raise ValueError("boom")
        with self.assertRaises(ValueError):
            await problem_async(5, f)

    async def test_concurrent_schedules(self):
        times = []
        def f(): times.append(time.monotonic())

        start = time.monotonic()
        await asyncio.gather(
            problem_async(20, f),
            problem_async(40, f),
            problem_async(10, f),
        )
        self.assertEqual(len(times), 3)
        elapsed_ms = [(t - start) * 1000.0 for t in times]
        self.assertGreaterEqual(min(elapsed_ms), 9.0)
        self.assertLess(max(elapsed_ms), 80.0)

if __name__ == "__main__":
    unittest.main()
