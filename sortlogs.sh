


#!/bin/bash

# Calculate the start and end times
start_time=$(date -d "+10 minutes" +%s)
end_time=$(date -d "+1 hour" +%s)

# Loop every 10 minutes until the end time
while [[ $(date +%s) -lt $end_time ]]; do
  # Get the last 15 lines of the Apache access log for 127.0.0.1
  tail -n 15 /var/log/apache2/access.log | grep "127.0.0.1" >> /tmp/filtered_localhost.log

  # Wait for 10 minutes
  sleep 600
done
