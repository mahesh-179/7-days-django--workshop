from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm
from django.contrib import messages

# # Simple test view
# def test(request):
#     return render(request, "tweets/index.html")


def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})
# Create a new tweet
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)  # handle image upload
        if form.is_valid():
            tweet = form.save()  # get model instance
            tweet.save()
            messages.success(request, "Tweet added successfully!")
            return redirect('tweet_list')    # redirect after saving
    else:
        form = TweetForm()  # empty form for GET request

    return render(request, 'tweets/tweet_form.html', {'form': form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet.save()
            messages.info(request, "Tweet updated!")
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweets/update.html', {'form': form})
         
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)

    if request.method == 'POST':
        tweet.delete()
        messages.error(request, "Tweet deleted!")
        return redirect('tweet_list')
    return render(request,"tweets/tweet_confirm.html",{'tweet':tweet})

def tweet_list(request):
    tweets = Tweet.objects.all()
    print("TOTAL:", tweets.count())
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})



    