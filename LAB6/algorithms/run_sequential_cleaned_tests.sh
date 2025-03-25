#!/bin/bash

echo "Running cleaned test suite 5 times..."
for i in {1..5}
do
    pytest --disable-warnings | tee -a sequential_final_results.txt
done

# Step 5: Extract execution times
echo "Extracting execution times..."
grep "seconds" sequential_final_results.txt | awk '{print $NF}' > times.txt

# Step 6: Compute Tseq (average execution time)
Tseq=$(awk '{sum+=$1} END {print sum/NR}' times.txt)
echo "Average Sequential Execution Time (Tseq): $Tseq seconds"

echo "Process completed successfully!"
