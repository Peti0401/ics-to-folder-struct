import os
import sys
from event import Event

# Reading the ics file and saving its lines into a list
with open("/Users/gyarmatip/Downloads/ww(1).ics") as file:
    lines = file.read().splitlines()

# A list which will hold groups of lines
line_groups = []
# Indices to track the beginning and end of the given events
begin_index = 0
end_index = 0

# Populating grouped_lines list
for index, line in enumerate(lines):
    if line.__contains__("BEGIN:VEVENT"):  # Beginning of event found
        begin_index = index
    elif line.__contains__("END:VEVENT"):  # End of event found
        end_index = index
        line_groups.append(lines[begin_index:end_index+1])

events = []
# constructing event objects from the line groups
for line_group in line_groups:
    event = Event()
    for line in line_group:
        # splitting the line at : to extract the current attribute's name and value
        key_value = line.split(':')
        # looping forward if the number of elements in the key_value list is not exactly 2
        if len(key_value) != 2:
            continue
        attr_name = key_value[0].lower()
        attr_value = key_value[1]
        # setting the attribute value reflectively
        setattr(event, attr_name, attr_value)
    events.append(event)

root_path = '/Users/gyarmatip/Documents/Coding/test-env/python-mkdirs'
# sub-directories can be specified
sub_dirs = ['s1', 's1/ss1', 's2', 's2/ss2']

# Actually creating folders
for event in events:
    # Formatting a date from 20191129T084500Z to 2019_11_19
    dir_name = '{}_{}_{}'.format(
        event.dtstart[0:4], event.dtstart[4:6], event.dtstart[6:8])
    dir_path = '{}/{}'.format(root_path, dir_name)
    print(dir_path)
    # Making the base directory
    # os.makedirs(dir_path)
    # Making all sub directories if specified
    print()
    for sub_dir in sub_dirs:
        sub_dir_path = '{}/{}'.format(dir_path, sub_dir)
        print(sub_dir_path)
        # os.makedirs(sub_dir_path)
    print()
