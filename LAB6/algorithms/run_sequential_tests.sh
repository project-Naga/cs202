#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run the test suite sequentially 10 times
echo "Running tests sequentially..."
for i in {1..10}
do
    pytest --disable-warnings >> sequential_results.txt
done

echo "Sequential test execution completed!"
