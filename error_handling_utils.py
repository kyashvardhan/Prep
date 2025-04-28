#!/usr/bin/env python3
"""
error_handling_utils.py
"""

import argparse
import random
import time
import logging
from contextlib import contextmanager
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

def retry(times=3, delay=1.0, exceptions=(Exception,)):
    """
    Decorator to retry a function upon exception.
    Args:
        times (int): Number of attempts (including the first).
        delay (float): Seconds to wait between retries.
        exceptions (tuple): Exception types to catch and retry on.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    logging.info(f"Attempt {attempt}/{times} for {fn.__name__}()")
                    return fn(*args, **kwargs)
                except exceptions as e:
                    last_exc = e
                    logging.warning(f"  Caught {type(e).__name__}: {e}")
                    if attempt < times:
                        logging.info(f"  Retrying after {delay}s...")
                        time.sleep(delay)
            logging.error(f"All {times} attempts failed for {fn.__name__}()")
            raise last_exc
        return wrapper
    return decorator

@contextmanager
def suppress_exceptions(*exc_types):
    """
    Context manager to suppress the specified exceptions.
    Usage:
        with suppress_exceptions(ValueError, KeyError):
            # code that may raise those, but won't propagate
    """
    try:
        yield
    except exc_types as e:
        logging.info(f"Suppressed {type(e).__name__}: {e}")

# --- Demo functions ---
def unstable_operation():
    """Simulates a function that fails randomly."""
    x = random.random()
    logging.info(f"  unstable_operation got value {x:.2f}")
    if x < 0.7:
        raise RuntimeError("Random failure occurred")
    return "Success!"

@retry(times=5, delay=0.5, exceptions=(RuntimeError,))
def retry_demo():
    """Demonstrate retrying an unstable operation."""
    result = unstable_operation()
    logging.info(f"Result: {result}")

def suppress_demo():
    """Demonstrate suppressing a ValueError."""
    logging.info("Entering suppress_demo()")
    with suppress_exceptions(ValueError):
        logging.info("  About to raise ValueError")
        raise ValueError("This will be suppressed")
    logging.info("Continued after suppression block")

# --- CLI Interface ---
def main():
    parser = argparse.ArgumentParser(description="Error handling utils demo")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("retry_demo", help="Run the retry decorator demo")
    sub.add_parser("suppress_demo", help="Run the suppress_exceptions demo")

    args = parser.parse_args()
    if args.cmd == "retry_demo":
        retry_demo()
    elif args.cmd == "suppress_demo":
        suppress_demo()

if __name__ == "__main__":
    main()
