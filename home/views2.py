from django.shortcuts import render
from django.http import StreamingHttpResponse
import os

def home(request):
    return render(request, 'home.html')

def stream_video(request, video_file_path):
    video_file = open(video_file_path, 'rb')
    response = StreamingHttpResponse(file_iterator(video_file))
    response['Content-Type'] = 'video/webm'
    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(video_file_path)
    response['Content-Length'] = os.path.getsize(video_file_path)

    if 'HTTP_RANGE' in request.META:
        range_header = request.META['HTTP_RANGE']
        start_range, end_range = parse_range_header(range_header, os.path.getsize(video_file_path))
        video_file.seek(start_range)
        response.status_code = 206
        response['Content-Range'] = 'bytes %s-%s/%s' % (start_range, end_range, os.path.getsize(video_file_path))
        response['Content-Length'] = end_range - start_range + 1
    else:
        video_file.seek(326402048)
        response.status_code = 206
        response['Content-Range'] = 'bytes 326402048-329562834/%s' % os.path.getsize(video_file_path)
        response['Content-Length'] = os.path.getsize(video_file_path) - 326402048

    return response

def parse_range_header(range_header, file_size):
    """
    Parse the Range header and return the start and end byte range
    """
    byte_range = range_header.split('=')[1]
    start_range, end_range = byte_range.split('-')
    if not start_range:
        # If the start byte range is not specified, return the end byte range
        start_range = file_size - int(end_range)
        end_range = file_size - 1
    else:
        start_range = int(start_range)
        if not end_range:
            end_range = file_size - 1
        else:
            end_range = int(end_range)
    return start_range, end_range

def file_iterator(file_obj, chunk_size=20000):
    """
    Read the file object in chunks and yield each chunk
    """
    while True:
        data = file_obj.read(chunk_size)
        if not data:
            break
        yield data
