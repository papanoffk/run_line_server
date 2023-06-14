from django.http import HttpResponse, FileResponse
from . import run_string_script
from django.conf import settings
from wsgiref.util import FileWrapper
import cv2, copy
import sys, os
sys.path.append("..")


# Create your views here.

def index(request):
    return HttpResponse("<h2>Введите текст</h2>")
def send_file(request):
    text = request.GET.get("text", 'Hello world!')
    path = os.path.abspath('run_string\\static\\img\\back100.png')
    path_to = os.path.abspath('run_string\\static\\video')

    run_string_script.draw(path, text, path_to)

    #draw('..\\static\\img\\back100.png', text)

    path_out = settings.BASE_DIR / 'run_string\\static\\video\\output.mp4'

    file = FileWrapper(open(path_out, 'rb'))
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
    return response

    #return HttpResponse(f"<h2>Имя: {print_string}</h2>")
