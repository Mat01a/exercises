#!/usr/bin/env bash

source_directory=/source/directory
target_directory=/target/directory

# current backup directory name
now=$(date +%Y-%m-%d)

count_backups=$(ls $target_directory | wc -l)

if [ $count_backups -gt 2 ]; then
	oldest_directory_name=$(ls -t $target_directory | tail -1)
	rm -r $target_directory/$oldest_directory_name
fi
rsync -av /$source_directory/ /$target_directory/$now/

exit 0;

