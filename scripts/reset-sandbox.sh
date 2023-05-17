#!/bin/bash
set -euo pipefail
echo "This will reset all lessons to their original state. Other files you have created in the free play mode stay intact. Are you sure you want to reset all lessons? [y/n]"

read choice

if [ "$choice" = 'y' ] || [ "$choice" = 'Y' ] ; then
    echo "Restoring your sandbox to its original state..."
    cp -r /var/backups/sandbox/workspaces /home/workspace/
    send-reset-sb-event
    echo "Done!"
else
    echo "Skipping reset. Your sandbox will remain in its current state."
fi;
