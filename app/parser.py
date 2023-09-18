import enum
import typing
from enum import Enum

CRLF = "\r\n"
CRLF_LEN = len(CRLF)

NUM_ELEMENTS_INDEX = 1


class RedisElementType(Enum):
    DATA_TYPE = enum.auto()


class RedisDataType(Enum):
    ARRAY = '*'
    BULK_STRING = '$'


def parse_request(request: bytes):
    decoded_request = request.decode()
    first_element, *rest = decoded_request.split(CRLF)

    # First element should identify the type
    first_type = parse_type(first_element)

    if first_type == RedisDataType.ARRAY:
        # TODO: Get number of elements from second character of first element
        num_elements = parse_num_elements(first_element)
        return parse_array(rest, num_elements)

    return first_type, rest


def parse_type(element: str):
    return RedisDataType(element[0])


def parse_num_elements(element: str):
    return int(element[NUM_ELEMENTS_INDEX])


# TODO: Unit test
def parse_array(elements: typing.List[str], num_elements: int):
    # TODO: Parse num_elements as items in array
    return num_elements, elements

