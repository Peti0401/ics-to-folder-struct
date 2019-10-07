import os
import sys
from event import Event


def read_file(file_path: str) -> list:
    '''
    Reads a file and returns its lines in a list
    :param str file_path: The full path to the file to be read
    :return: the lines of the file in a list
    :rtype: list
    '''
    with open(file_path) as file:
        lines = file.read().splitlines()
    return lines


def group_lines(ics_file_lines: list) -> list:
    '''
    Creates line groups from the lines of an ics file, such that each line group (sub-list)
    contains all details about a single event
    :param list ics_file_lines: The lines of an ics file as a list
    :return: A two-dimensional list, a list of line groups
    :rtype: list
    '''
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


def construct_single_event(line_group: list) -> Event:
    '''
    Constructs an Event object from a group of ics file lines.
    The lines should contain the attribute names and values of an event
    :param list line_group: A list of ics file lines
    :return: An Event object
    :rtype: Event
    '''
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


def construct_events(line_groups: list) -> list:
    '''
    Constructs Event objects from a list of groups of ics file lines.
    :param list line_groups: A list of lists of ics file lines
    :return: A list of Event object
    :rtype: list
    '''
    events = []
    # constructing event objects from the line groups
    for line_group in line_groups:
        event = construct_single_event(line_group)
        events.append(event)
    return events


def format_event_date(date: str) -> str:
    return '{}_{}_{}'.format(date[0:4], date[4:6], date[6:8])


def construct_directories(ics_file_path: str, root_dir_path: str, sub_dirs: list, files: list):
    '''
    Creates directories on the platform by processing the ics file.
    Base directories will be created as children of the directory at root_dir_path.
    Each base directory will correspond to a specific event's start date (dtstart) attribute value.
    Sub-directories can be specified to be included into the base directories.
    :param str ics_file_path: Path to the ics file
    :param str root_dir_path: Path to the enclosing directory (gets created if not exists)
    :param list sub_dirs: A list of sub-directories relative to root_dir_path
    :param list files: A list of files which will get created in each directory
    '''
    ics_file_lines = read_file(ics_file_path)
    line_groups = group_lines(ics_file_lines)
    events = construct_events(line_groups)
    for event in events:
        # Formatting a date from 20191129T084500Z to 2019_11_19
        dir_name = format_event_date(event.dtstart)
        dir_path = '{}/{}'.format(root_dir_path, dir_name)
        # Making the base directory
        os.makedirs(dir_path, exist_ok=True)

        # Making all sub directories if specified
        for sub_dir in sub_dirs:
            sub_dir_path = '{}/{}'.format(dir_path, sub_dir)
            os.makedirs(sub_dir_path, exist_ok=True)

        # Creating the specified files
        for file in files:
            file_path = '{}/{}'.format(dir_path, file)
            open(file_path, "w")
