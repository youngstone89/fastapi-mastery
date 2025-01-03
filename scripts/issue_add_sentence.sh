#!/bin/bash

# Number of parallel runs
NUM_RUNS=1

# Define the curl command
CURL_COMMAND="curl --location --request POST 'http://127.0.0.1:8000/semantic_search/add-sentence?text=It%20is%20a%20long%20established%20fact%20that%20a%20reader%20will%20be%20distracted%20by%20the%20readable%20content%20of%20a%20page%20when%20looking%20at%20its%20layout.%20The%20point%20of%20using%20Lorem%20Ipsum%20is%20that%20it%20has%20a%20more-or-less%20normal%20distribution%20of%20letters%2C%20as%20opposed%20to%20using%20%27Content%20here%2C%20content%20here%27%2C%20making%20it%20look%20like%20readable%20English.%20Many%20desktop%20publishing%20packages%20and%20web%20page%20editors%20now%20use%20Lorem%20Ipsum%20as%20their%20default%20model%20text%2C%20and%20a%20search%20for%20%27lorem%20ipsum%27%20will%20uncover%20many%20web%20sites%20still%20in%20their%20infancy.%20Various%20versions%20have%20evolved%20over%20the%20years%2C%20sometimes%20by%20accident%2C%20sometimes%20on%20purpose%20(injected%20humour%20and%20the%20like).%0A%0A' \
--data ''"

# Function to execute the curl command
run_curl() {
    eval "$CURL_COMMAND"
}

# Export the function for parallel execution
export -f run_curl
export CURL_COMMAND

# Run the command in parallel
seq $NUM_RUNS | xargs -n1 -P$NUM_RUNS -I{} bash -c 'run_curl'
