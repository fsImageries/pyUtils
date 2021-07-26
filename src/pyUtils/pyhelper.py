from string import digits
from time import time, sleep
from collections import Iterable

import os
import sys
import json
import static
import socket
import traceback

try:
    from os import scandir
except ImportError:
    try:
        from scandir import scandir
    except ImportError:
        scandir = None


# ------------------------- PySide2 Client ---------------------------- #
# --------------------------------------------------------------------- #


class ClientBase(object):

    PORT = static.PORT
    HEADER_SIZE = static.HEADER_SIZE

    def __init__(self, timeout=2):
        self.timeout = timeout
        self.port = self.__class__.PORT

        self.discard_count = 0

    def connect(self, port=-1):
        if port >= 0:
            self.port = port

        try:
            self.client_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((static.HOST, self.port))
        except:
            traceback.print_exc()
            return False

        return True

    def disconnect(self):
        try:
            self.client_socket.close()
        except:
            traceback.print_exc()
            return False

        return True

    def send(self, data, json_cls=None):
        json_data = json.dumps(data, cls=json_cls)

        message = list()
        message.append("{0:10d}".format(len(json_data.encode())))
        message.append(json_data)

        while True:
            try:
                msg_str = "".join(message)
                self.client_socket.sendall(msg_str.encode())

                # we assume a return dict with the key 'success' exists
                # and got a truthy value when everything went right
                ret_data = self.client_socket.recv(4096)
                ret_data = json.loads(ret_data[10:])
                if ret_data.get("success", None):
                    break
            except:
                traceback.print_exc()
                return None

    def recv(self):
        total_data = list()
        data = ""
        reply_length = 0
        bytes_remaining = ClientBase.HEADER_SIZE

        start_time = time()
        while time() - start_time < self.timeout:
            try:
                data = self.client_socket.recv(bytes_remaining)
            except Exception as e:
                print("Exception: {}".format(e))
                sleep(0.01)
                continue

            if data:
                total_data.append(data)

                bytes_remaining -= len(data)
                if(bytes_remaining <= 0):
                    for i in range(len(total_data)):
                        total_data[i] = total_data[i].decode()

                    if reply_length == 0:
                        header = "".join(total_data)
                        reply_length = int(header)
                        bytes_remaining = reply_length
                        total_data = list()
                    else:
                        reply_json = "".join(total_data)
                        return json.loads(reply_json)

        raise RuntimeError("[ERROR] Timeout waiting for response.")

    def is_valid_data(self, data):
        if not data:
            print("[ERROR] Invalid Data.")
            return False

        if not data["success"]:
            print("[ERROR] {0} failed: {1}".format(data["cmd"], data["msg"]))
            return False

        return True

    def ping(self):
        data = {"cmd": "ping"}
        reply = self.send(data)

        if self.is_valid_data(reply):
            return True
        return False


# --------------------- Python Helper Functions ----------------------- #
# --------------------------------------------------------------------- #


def filename_from_path(filepath):
    """
    Get the file name without extension from a file path.

    Args:
        filepath ([String]): Path to desired file.

    Returns:
        [String]: File name without extension.
    """
    return os.path.splitext(os.path.basename(filepath))[0]


def basename_plus(filepath):
    """ Get every property of a filename as item """

    # Split of standard properties.
    basedir, filename = os.path.split(filepath)
    name_noext, ext = os.path.splitext(filename)

    # Split of Digits at the end of string. Useful for a name of a sequence i.e. Image Sequence.
    digitsChars = digits.encode()
    name_nodigits = name_noext.rstrip(digitsChars) if name_noext.rstrip(
        digitsChars) != name_noext else None

    return name_noext, name_nodigits, basedir, ext


def get_img_seq(filepath):
    """ Get list with all images of a chosen picture """

    # Get Filename with and without padding, Directory of the file and extension.
    _, filename_nodigits, basedir, ext = basename_plus(filepath)

    # Check if Input is part of a
    if filename_nodigits is None:
        return []

    # Scan the directory for every file that has the same Name and Extension and check if it has padding.
    # If so add to frames.
    frames = [
        f.path for f in scandir(basedir) if
        f.is_file() and
        f.name.startswith(filename_nodigits) and
        f.name.endswith(ext) and
        f.name[len(filename_nodigits):-len(ext) if ext else -1].isdigit()]

    # Check if frames has more than one Image, if so return sorted frames.
    if len(frames) > 1:
        return sorted(frames)

    return []


def get_padded_names(name, padding, sequenceLen):

    if padding == 0:
        padVal = len(str(sequenceLen))
    else:
        padVal = padding

    padding = ["%s%s" % ("0" * (padVal - len(str(num))), num)
               for num in range(0, sequenceLen)]

    final = ["%s_%s" % (name, pad) for pad in padding]

    return final


def flatten(src_list):
    """
    Basic List flattening, supports Lists, Tuples and Dictionaries.

    It checks for iter attribute and goes recursively over every item. It stores matches into a new List.
    When Dictionary it gets the items and calls itself to flatten them like a normal List.
    When no type is valid return the Item in a new List.

    Args:
        src_list ([Iterable]): The Source List which should be flattened.

    Returns:
        [List]: Returns the flattened List.
    """
    if any(isinstance(x, Iterable) for x in src_list):

        if isinstance(src_list, dict):
            return flatten(src_list.items())

        flat_sum = flatten(
            src_list[0]) + (flatten(src_list[1:]) if len(src_list) > 1 else[])
        return flat_sum

    elif isinstance(src_list, Iterable):
        return src_list

    return [src_list]


def listsplit_gap(li):
    """
    Split a list by the numeric gap between it's elements. Only works on interger lists.

    Args:
        li ([List]): List which should be splited.

    Returns:
        [List]: Splited list.
    """
    # Determine where the gaps are occurring
    gap_loc = [idx + 1
               for (idx, el), next_el in zip(enumerate(li[:-1]), li[1:])
               if (next_el - el) > 1]
    # Adding beginning and end of the list
    gap_loc.insert(0, 0)
    gap_loc.append(len(li))
    # Create sublists where gaps occurs
    list_seq = [li[prev_gap:gap]
                for prev_gap, gap in zip(gap_loc[:-1], gap_loc[1:])]

    return list_seq


def join_recursive(p1, ps):
    try:
        pnew = ps[0]
        p1new = os.path.join(p1, pnew)
        ps.pop(0)
        return join_recursive(p1new, ps)
    except IndexError:
        return p1


# ------------------------ Context Managers --------------------------- #
# --------------------------------------------------------------------- #


class FunctionTimer(object):
    def __enter__(self):
        self.start_time = time()

    def __exit__(self, *_):
        print("My program took", time() - self.start_time, "to run")


# ---------------------------- Scripts -------------------------------- #
# --------------------------------------------------------------------- #


def folder_creator(path, name, folders, post=None):
    print(path)
    print(name)
    path = os.path.join(path, name)
    os.mkdir(path)

    for f in folders:
        dirs = f.split("/")
        add = ""
        for d in dirs:
            add = os.path.join(add, d)
            dpath = os.path.join(path, add)

            try:
                os.mkdir(dpath)
            except FileExistsError:
                continue

    if post:
        post(path)


def workspace_mel(path):
    """
    Create a 'workspace.mel' at the given path.

    Args:
        path ([Str]): Path to the project folder where the workspace.mel should be placed.
    """
    with open(os.path.join(path, "workspace.mel"), "w") as f:
        f.write(static.workspace_definition.strip())


if __name__ == "__main__":
    path = sys.argv[1]
    name = sys.argv[2]
    folder_creator(path, name, static.project_folders, post=workspace_mel)
