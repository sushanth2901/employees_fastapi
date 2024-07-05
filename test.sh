#bin/bash

CPU_THRESHOLD=2
MEMORY_THRESHOLD=4

EMAIL_RECIPIENTS="sushanth.tudi@modak.com"
EMAIL_SUBJECT="Resource Utilization Alert"

CPU_UTILIZATION=$(vmstat 1 2 | tail -1 | awk '{print 100 - $15}')

MEMORY_UTILIZATION=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

echo "Current CPU Utilization: ${CPU_UTILIZATION}%"
echo "Current Memory Utilization: ${MEMORY_UTILIZATION}%"

if (( $(echo "$CPU_UTILIZATION > $CPU_THRESHOLD" | bc -l) )) || (( $(echo "$MEMORY_UTILIZATION > $MEMORY_THRESHOLD" | bc -l) )); then
    echo "Threshold exceeded, sending email notification."
    echo -e "Resource Utilization Alert:\n\nCPU Utilization: ${CPU_UTILIZATION}%\nMemory Utilization: ${MEMORY_UTILIZATION}%\n\nOne or both of these metrics have exceeded their respective thresholds." | mail -s "$EMAIL_SUBJECT" "$EMAIL_RECIPIENTS"
else
    echo "Resource utilization is within acceptable limits."
fi
