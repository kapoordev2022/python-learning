from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": None,
    "february": "Hello, February!",
    "march": "Hello, March!",
    "april": "Hello, April!",
    "may": "Hello, May!",
    "june": "Hello, June!",
    "july": "Hello, July!",
    "august": "Hello, August!",
    "september": "Hello, September!",
    "october": "Hello, October!",
    "november": "Hello, November!",
    "december": "Hello, December!",
}

def index(request):
    return render(request, "challenges/index.html", {
        "months": monthly_challenges.keys()
    })

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenges.html", {
             "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()
        
def monthly_challenge_by_number(request, month):
    try:
        challenge_text = list(monthly_challenges.keys())
        if month > len(challenge_text):
            return HttpResponseNotFound("This month is not supported!")
        forword_month = challenge_text[month - 1]
        redirect_path = reverse("month-challenge", args=[forword_month])
        return HttpResponseRedirect(redirect_path)
    except:
        raise Http404()