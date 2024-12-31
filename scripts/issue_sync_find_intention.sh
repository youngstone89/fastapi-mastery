#!/bin/bash

# Number of parallel runs
NUM_RUNS=5

# Define the curl command
CURL_COMMAND="curl --location 'http://127.0.0.1:8000/semantic_search/sync-find-intention?query=Lorem%20Ipsum%20is%20simply%20dummy%20text%20of%20the%20printing%20and%20typesetting%20industry.%20Lorem%20Ipsum%20has%20been%20the%20industry%27s%20standard%20dummy%20text%20ever%20since%20the%201500s%2C%20when%20an%20unknown%20printer%20took%20a%20galley%20of%20type%20and%20scrambled%20it%20to%20make%20a%20type%20specimen%20book.%20It%20has%20survived%20not%20only%20five%20centuries%2C%20but%20also%20the%20leap%20into%20electronic%20typesetting%2C%20remaining%20essentially%20unchanged.%20It%20was%20popularised%20in%20the%201960s%20with%20the%20release%20of%20Letraset%20sheets%20containing%20Lorem%20Ipsum%20passages%2C%20and%20more%20recently%20with%20desktop%20publishing%20software%20like%20Aldus%20PageMaker%20including%20versions%20of%20Lorem%20Ipsum.'"

# Function to execute the curl command
run_curl() {
    eval "$CURL_COMMAND"
}

# Export the function for parallel execution
export -f run_curl
export CURL_COMMAND

# Start the timer
start_time=$(date +%s)

# Run the command in parallel
seq $NUM_RUNS | xargs -n1 -P$NUM_RUNS -I{} bash -c 'run_curl'

# End the timer
end_time=$(date +%s)

# Calculate and display the total execution time
execution_time=$((end_time - start_time))
echo ""
echo "Total execution time: ${execution_time} seconds"
