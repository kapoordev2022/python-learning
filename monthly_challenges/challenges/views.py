from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Hello, January!",
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


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")

def monthly_challenge_by_number(request, month):
    try:
        challenge_text = list(monthly_challenges.keys())
        if month > len(challenge_text):
            return HttpResponseNotFound("This month is not supported!")
        forword_month = challenge_text[month]
        return HttpResponseRedirect("/challenges/" + forword_month)
    except:
        return HttpResponseNotFound("This month is not supported!")