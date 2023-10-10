# urine_strip_app/views.py

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import numpy as np
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from django.shortcuts import render


@csrf_exempt
@require_POST
def process_urine_strip(request):
    image = request.FILES['image']
    # create a numpy array from the image
    image_array = np.array(Image.open(image))
    num_pixels = image_array.shape[0] * image_array.shape[1]
    image_array_reshaped = image_array.reshape(num_pixels, -1)
    num_colors = 10
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(image_array_reshaped)
    colors = kmeans.cluster_centers_
    colors = colors.astype(int)
    result = []
    for color in colors:
        result.append(color.tolist())
    
    return JsonResponse({'colors': result})


# render the index.html template as the root URL
def index(request):
    return render(request, 'index.html')