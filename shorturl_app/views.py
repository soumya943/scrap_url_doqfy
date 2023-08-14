# # views.py
# from django.shortcuts import render, redirect
# from .models import ShortURL
# from .forms import ShortURLForm
# import random, string
# import json
# from django.http import JsonResponse
# # import redis

# def generate_short_code():
#     chars = string.ascii_letters + string.digits
#     return ''.join(random.choice(chars) for _ in range(6))

# def create_short_url(request):
#     if request.method == 'POST':
#         form = ShortURLForm(request.POST)
#         if form.is_valid():
#             original_url = form.cleaned_data['original_url']
#             short_code = generate_short_code()
#             short_url = ShortURL(original_url=original_url, short_code=short_code)
#             short_url.save()
#             return render(request, 'success.html', {'short_url': short_url})
#     else:
#         form = ShortURLForm()
#     return render(request, 'create.html', {'form': form})



# # def display_data(request):
# #     redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# #     data = redis_client.get('nifty_data')
# #     if data:
# #         data = json.loads(data)
# #         return JsonResponse(data, safe=False)
# #     else:
# #         return JsonResponse({"error": "Data not available"}, status=404)


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortURL
import random
import string

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def index(request):
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        short_code = generate_short_code()
        ShortURL.objects.create(original_url=original_url, short_code=short_code)
        return render(request, 'index.html', {'short_code': short_code})
    return render(request, 'index.html')

def redirect_to_full_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.original_url)



from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Snippet
from cryptography.fernet import Fernet
from cryptography. fernet import Fernet 

def generate_secret_key():
    return Fernet.generate_key()

def create_snippet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        secret_key = request.POST.get('secret_key', '')
        snippet = Snippet.objects.create(content=content, secret_key=secret_key)
        return render(request, 'create_snip.html', {'snippet_id': snippet.id})

        # return redirect('view_snippet', snippet_id=snippet.id)
    
    return render(request, 'create_snip.html')

def redirect_to_full_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.original_url)

def view_snippet(request, snippet_id):

    if request.method == 'POST':
        snippet = get_object_or_404(Snippet, id=snippet_id)
        secret_key = request.POST.get('secret_key', '')
        print(secret_key)
        print(snippet.secret_key)
        if secret_key==snippet.secret_key:
            fernet = Fernet( b'WHPfvcJJbYOvJn5Ar9tPb8X8aYE776gKweaIv9bK0vg=')
            print(fernet)
            decrypted_content=snippet.content
            # decrypted_content = fernet.decrypt(snippet.content.encode()).decode()
        else:
            decrypted_content = "Error: Invalid key or content"

        return render(request, 'view_snip.html', {'decrypted_content': decrypted_content})
    
    return render(request, 'view_snip.html')


import threading
from django.shortcuts import render
from django.core.cache import cache

from .utils import *
from shorturl_project.task import *
def display_data(request):    
    # scrape_nifty_data()
    nifty_data = cache.get('nifty_data', [])
    print(nifty_data)
    return render(request, 'scrap.html', {'nifty_data': nifty_data})

