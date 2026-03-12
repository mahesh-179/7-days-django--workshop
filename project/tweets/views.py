from django.shortcuts import render,get_object_or_404,redirect
from .models import tweets
from .forms import TweetForm

# Create your views here.
def test(request):
    return render(request,"tweets/index.html")


def tweet_list(request):
   Tweets = tweets.objects.all().order_by('-created_at')
   return render(request,'tweets/tweets.html',{'Tweets':Tweets})

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)  # handle image upload
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user  # assign logged-in user
            tweet.save()
            return redirect('tweet_list')  # redirect after saving
    else:
        form = TweetForm()  # only create empty form if GET request

    return render(request, 'tweets/tweet_form.html', {'form': form})