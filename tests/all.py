import unittest
import colour_runner.runner

# Load all tests in this directory
loader = unittest.TestLoader()
suite = loader.discover('.')

# Run all tests
runner = colour_runner.runner.ColourTextTestRunner(verbosity=2)
runner.run(suite)

