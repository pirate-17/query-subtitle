from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import VideosForm, SearchForm
from django.core.files.storage import default_storage
from . import process_subtitles
from videos import tasks
import os
from django.contrib import messages



def home(request):
    # home page view
    form = None
    if request.method == 'POST':
        form = VideosForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            print('Form validation done')
            # form.save()
            file = request.FILES['file']
            file_name = default_storage.save(file.name, file)

            file_url = default_storage.url(file_name)
            # Extract subtitles from the video
            # get the path of the saved video
            print(file_url)

            print()
            print()
            print()


            path = form.cleaned_data['file'].name
            print(path)
            return HttpResponse('The video was uploaded sucessfully and is being processed...')
    else:
        form = VideosForm()
    return render(request, 'home.html', {'form': VideosForm})


def upload_file(request):
    submitted = False

    if request.method == 'POST':
        form = VideosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Build paths inside the project like this: BASE_DIR / 'subdir'.
            BASE_DIR = os.getcwd()
            MEDIA_DIR = os.path.join(BASE_DIR, 'videos', 'media')

            subtitle_file_name = process_subtitles.extract_subtitles(MEDIA_DIR, request.FILES['file'].name)
            subtitle_file_path = os.path.join(MEDIA_DIR, subtitle_file_name)

            tasks.upload_file.delay(subtitle_file_path)

            form = SearchForm()
            return HttpResponseRedirect('/search_keywords?submitted=True&st={subtitle_file_name}')
    else:
        form = VideosForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'home.html', {'form': form, 'submitted':submitted})

def search_keyword(request):
    if request.method == 'POST':
        form = SearchForm(request.POST, request.FILES)
        # get the st parameter from payload
        # st = request.POST['st']

        print('passed st at the end')
        print()
        print(request.payload)
        print()
        if form.is_valid():
            form.save()
            keyword = request.POST['search_keyword']
            print(keyword)
            tasks.upload_search_keywords.delay(keyword)
            print()
            print()
            print(temp_subtitle_path)
            print()
            response = process_subtitles.search_keyword_in_subtitles(temp_subtitle_path, keyword)
            messages.success(request, response)
    else:
        form = SearchForm()
        if 'st' in request.GET:
            st = request.GET['st']
            
    return render(request, 'search.html', {'form': form, 'st': st})
