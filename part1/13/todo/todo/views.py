import os.path

import requests
from django.views.generic import TemplateView
import datetime
from django.conf import settings
import glob


TIME_FORMAT = '%Y-%m-%d-%H:%M:%S.jpg'
IMAGE_PATH_GLOB = ''.join([settings.MEDIA_ROOT, '*.jpg'])


def get_or_create_image():
    """
    Let's implement image cache that is independent of the state of the Django application
    and only on the state of file storage.
    Use a filename to differentiate.
    """
    now_time = datetime.datetime.now()
    images = glob.glob(IMAGE_PATH_GLOB)
    if len(images) > 0:
        image_name = os.path.basename(images[0])
        image_time = datetime.datetime.strptime(image_name, TIME_FORMAT)
        difference_in_minutes = (now_time - image_time).total_seconds() / 60
        if difference_in_minutes >= settings.IMAGE_LIFE_MINUTES:
            for image in images:
                os.remove(image)
            return create_image(now_time)
        else:
            return os.path.join(settings.MEDIA_URL, image_name)
    else:
        return create_image(now_time)

def create_image(now_time):
    r = requests.get(settings.IMAGE_SOURCE_URL)
    file_name = now_time.strftime(TIME_FORMAT)
    path = os.path.join(settings.MEDIA_ROOT, file_name)
    with open(path, 'wb') as f:
        f.write(r.content)
    url = os.path.join(settings.MEDIA_URL, file_name)
    return url


class RootView(TemplateView):
    template_name = 'root.html'
    def get_context_data(self, **kwargs):
        context = super(RootView, self).get_context_data(**kwargs) # get the default context data
        context['image_url'] = get_or_create_image()

        return context