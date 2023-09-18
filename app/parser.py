import typing
from enum import Enum

CRLF = "\r\n"
CRLF_LEN = len(CRLF)


class RedisDataType(Enum):
    ARRAY = ord('*')
    BULK_STRING = ord('$')


def parse_data_type(byte: int):
    return RedisDataType(byte)


def parse_element_type(array):
    num_elements_byte, *rest = array
    num_elements = int(chr(num_elements_byte))
    return num_elements, rest


def parse_array(array: typing.List[int]):
    num_elements, rest = parse_element_type(array)

    # TODO: Yield return the results
    for i in range(num_elements):
        # Skip CRLF
        rest = rest[CRLF_LEN:]

        # Parse the next element
        next_type_byte, *rest = rest
        next_element_type = parse_data_type(next_type_byte)
        print("Next element type: {}".format(next_element_type))

        if next_element_type == RedisDataType.ARRAY:
            return parse_array(rest)
        elif next_element_type == RedisDataType.BULK_STRING:
            return parse_bulk_string(rest)

        rest_as_bytes = bytes(rest)
        print("Rest in array: {}".format(rest_as_bytes))


def parse_bulk_string(rest: typing.List[int]):
    num_elements, rest = parse_element_type(rest)
    print("Number of elements: {}".format(num_elements))

    # TODO: Skip CRLF

    rest_as_bytes = bytes(rest)
    print("Rest in bulk string: {}".format(rest_as_bytes))
