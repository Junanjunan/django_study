from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, FileResponse, StreamingHttpResponse
from django.core.files import File
from wsgiref.util import FileWrapper
import os
import mimetypes
from .models import *
import time
from datetime import time as time_


def home(request):
    full_time = 548
    minutes, r_seconds = divmod(full_time, 60)
    hours, r_minutes = divmod(minutes, 60)
    if hours == 0:
        staying_time = time_(minute=r_minutes, second=r_seconds)
    else:
        staying_time = time_(hour=hours, minute=r_minutes, second=r_seconds)
    print(staying_time)
    print(type(staying_time))
    home_object = Home.objects.first()
    home_object.staying_time = staying_time
    home_object.save()
    print(home_object.staying_time)

    return render(request, 'home.html')


def dot_5():
    time.sleep(0.05)
    return

def crawl_reallinux(request):
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    with open("cr.text", 'w') as file:
        
        url = 'https://www.reallinux.co.kr/realacademy/'
        driver = webdriver.Chrome()
        driver.get(url)
        driver.find_element(By.CLASS_NAME, 'v-app-bar__nav-icon').click()
        # course_click_list = ['1. 리눅스 교육', '3. 온라인 임베디드 교육', '4. 온라인 서버엔지니어 교육']
        course_click_list = driver.find_elements(By.CLASS_NAME, 'v-list-group')
        dot_5()
        for course in course_click_list:
            time.sleep(1)
            course.click()
            curris = [tag for tag in course.find_elements(By.CLASS_NAME, 'v-list-item--link') if tag.get_attribute('role') == 'listitem']
            
            dot_5()
            for curri in curris:
                time.sleep(1)
                curri.click()
                print("curri: ",curri.text)
                file.write(f"curri: {curri.text} \n")
                dot_5()
                driver.find_element(By.CLASS_NAME, 'v-overlay__scrim').click()
                parts = driver.find_elements(By.CLASS_NAME, 'v-expansion-panel')
                for part in parts:
                    if part.get_attribute('aria-expanded') == 'false':
                        part.click()
                    print("part:", part.find_element(By.CLASS_NAME, 'v-expansion-panel-header').text)
                    file.write(f"part: {part.find_element(By.CLASS_NAME, 'v-expansion-panel-header').text} \n")
                    dot_5()
                    contents = part.find_elements(By.CLASS_NAME, 'v-btn__content')
                    for content in contents:
                        if 'play_circle' in content.text:
                            continue
                        print("content:", content.text)
                        file.write(f"content: {content.text} \n")
                        dot_5()
                dot_5()
                driver.find_element(By.CLASS_NAME, 'v-app-bar__nav-icon').click()
            time.sleep(1)
            print("-------------------------")
            file.write("--------------------")
    print("---0-----")
    driver.close()
    return render(request, 'home.html')


def video_test(request):
    return render(request, 'video_test.html')


def get_video_url(token):
    # Here, you should add the logic to get the URL of the video based on the token.
    # This could involve looking up the token in a database, or constructing the URL
    # based on some other criteria.
    # For the purpose of this example, let's just return a hardcoded URL.
    video_file_path = '/static/media/linux.mp4'
    path_joined = os.path.join(os.getcwd(), video_file_path)
    return path_joined


def token_video(request):
    video_file_path = '/static/media/linux.mp4'
    path_joined = os.path.join(os.getcwd(), video_file_path)

    def file_iterator(file_path, chunk_size=8192):
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                yield data


    response = StreamingHttpResponse(file_iterator(path_joined))
    response['Content-Type'] = mimetypes.guess_type(path_joined)[0]
    response['Content-Length'] = os.path.getsize(path_joined)
    response['content-Disposition'] = 'inline'
    response['X-Accel-Redirect'] = os.path.join('/internal-videos', os.path.basename(path_joined))
    
    return response

    




def stream_video(request):

    video_file_path = 'linux.mp4'
    path_joined = os.path.join(os.getcwd(), video_file_path)
    video_file = open(path_joined, 'rb')
    response = StreamingHttpResponse(file_iterator(video_file))
    response['Content-Type'] = 'video/mp4'
    response['Content-Length'] = os.path.getsize(video_file_path)
    response['Content-Disposition'] = 'inline'

    if 'HTTP_RANGE' in request.META:
        range_header = request.META['HTTP_RANGE']
        start_range, end_range = parse_range_header(range_header, os.path.getsize(video_file_path))
        video_file.seek(start_range)
        response.status_code = 206
        response['Content-Range'] = 'bytes %s-%s/%s' % (start_range, end_range, os.path.getsize(video_file_path))
        response['Content-Length'] = end_range - start_range + 1
    else:
        video_file.seek(0)
        response.status_code = 200

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


def file_iterator(file_obj, chunk_size=3000):
    """
    Read the file object in chunks and yield each chunk
    """
    while True:
        data = file_obj.read(chunk_size)
        if not data:
            break
        yield data




