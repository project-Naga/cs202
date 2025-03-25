#!/bin/bash

source venv/bin/activate

echo "Running parallel tests with pytest-xdist (load)..."
for i in {1..3}
do
    pytest -n auto --dist load --disable-warnings >> parallel_load_results.txt
done

echo "Running parallel tests with pytest-xdist (no)..."
for i in {1..3}
do
    pytest -n auto --dist no --disable-warnings >> parallel_no_results.txt
done

echo "Running parallel tests with pytest-run-parallel..."
for i in {1..3}
do
    pytest --parallel-threads auto --disable-warnings >> parallel_threads_results.txt
done

echo "Parallel test execution completed!"
