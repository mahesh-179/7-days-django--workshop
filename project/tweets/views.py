from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm, UserRegister
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# 🔹 Show all tweets (latest first)
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/tweet_list.html', {'tweets': tweets})


# 🔹 Create a new tweet
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)   # don't save yet
            tweet.user = request.user         # ⭐ assign logged-in user
            tweet.save()
            messages.success(request, "Tweet added successfully!")
            return redirect('tweet_list')
    else:
        form = TweetForm()

    return render(request, 'tweets/tweet_form.html', {'form': form})


# 🔹 Edit tweet (only owner can edit)
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            messages.info(request, "Tweet updated!")
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'tweets/update.html', {'form': form})


# 🔹 Delete tweet (only owner can delete)
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        tweet.delete()
        messages.error(request, "Tweet deleted!")
        return redirect('tweet_list')

    return render(request, "tweets/tweet_confirm.html", {'tweet': tweet})


# 🔹 Register new user
def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created Successfully")
            return redirect('tweet_list')
    else:
        form = UserRegister()

    return render(request, 'registeration/register.html', {'form': form})