# -*- coding: utf-8 -*-
from base64 import b64decode


def decode_base64(filedata):
    if not (filedata or filedata.get('base64')):
        return "No base64 file data provided"
    else:
        # {
        #     "filesize": 54836, / * bytes * /
        # "filetype": "image/jpeg",
        #             "filename": "profile.jpg",
        #                         "base64":   "/9j/4AAQSkZJRgABAgAAAQABAAD//gAEKgD/4gIctcwIQA..."
        # }
        file_name = filedata.get('filename')
        file_ext = filedata.get('filetype')
        file_size = filedata.get('filesize')
        decoded_file = filedata.get('base64')

        try:
            b64decode(decoded_file)
