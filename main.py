import os
import sys
from event import Event


def read_file(file_path: str) -> list:
    with open(file_path) as file:
        lines = file.read().splitlines()
    return lines


# Returns a list of lists which include the lines of an event
def group_lines(ics_file_lines: list) -> list:
    # A list which will hold groups of lines
    line_groups = []

    # Indices to track the beginning and end of the given events
    begin_index = 0
    end_index = 0

    # Populating grouped_lines list
    for index, line in enumerate(ics_file_lines):
        if line.__contains__("BEGIN:VEVENT"):  # Beginning of event found
            begin_index = index
        elif line.__contains__("END:VEVENT"):  # End of event found
            end_index = index
            line_groups.append(ics_file_lines[begin_index:end_index+1])
    return line_groups


# Constructs a single event object from a line group, which holds all the attribute name - value pairs
def construct_single_event(line_group: list) -> Event:
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
    return event


# Constructs a list of events from multiple line groups
def construct_events(line_groups: list) -> list:
    events = []
    # constructing event objects from the line groups
    for line_group in line_groups:
        event = construct_single_event(line_group)
        events.append(event)
    return events


def construct_directories(ics_file_lines: list, root_dir_path: str, sub_dirs: list):
    line_groups = group_lines(ics_file_lines)
    events = construct_events(line_groups)
    for event in events:
        # Formatting a date from 20191129T084500Z to 2019_11_19
        dir_name = format_event_date(event.dtstart)
        dir_path = '{}/{}'.format(root_dir_path, dir_name)
        # Making the base directory
        # os.makedirs(dir_path)
        # Making all sub directories if specified
        for sub_dir in sub_dirs:
            sub_dir_path = '{}/{}'.format(dir_path, sub_dir)
            print(sub_dir_path)
            # os.makedirs(sub_dir_path)


def format_event_date(date: str) -> str:
    return '{}_{}_{}'.format(date[0:4], date[4:6], date[6:8])


# Main
ics_file_path = '/Users/gyarmatip/Downloads/ww(1).ics'
ics_file_lines = read_file(ics_file_path)
root_dir_path = '/Users/gyarmatip/Documents/Coding/test-env/python-mkdirs'
sub_dirs = ['Literatur', 'Folien']
construct_directories(ics_file_lines, root_dir_path, sub_dirs)
