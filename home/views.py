from django.shortcuts import render, redirect, get_object_or_404  # Import necessary functions
from django.contrib.auth import authenticate, login, logout  # Import authentication functions
from django.contrib import messages  # Import messages framework for user feedback
from django.contrib.auth.decorators import login_required  # Restrict access to logged-in users
from django.db.models import Count  # Import Count function to count votes
from .models import Candidate, Vote  # Import Candidate and Vote models

# ✅ Home Page
def index(request):
    return render(request, "index.html")

# ✅ About Page
def about(request):
    return render(request, "about.html")

# ✅ Contact Page
def contact(request):
    return render(request, "contact.html")

# ✅ Help Page
def help(request):
    return render(request, "help.html")

# ✅ Login View
def login_view(request):
    if request.method == "POST":
        voter_id = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=voter_id, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "✅ Login successful!")
            return redirect("vote")
        else:
            messages.error(request, "❌ Invalid Voter ID or password!")

    return render(request, "login.html")

@login_required
def vote(request):
    candidates = Candidate.objects.annotate(vote_count=Count("vote"))
    
    # ✅ Check if user already voted
    if Vote.objects.filter(user=request.user).exists():
        messages.warning(request, "❌ You have already voted!")
        return redirect("result")

    if request.method == "POST":
        candidate_id = request.POST.get("candidate_id")  
        print(f"📩 Received Vote: User={request.user}, Candidate ID={candidate_id}")

        if not candidate_id:
            messages.error(request, "❌ Please select a candidate to vote!")  
            return redirect("vote")

        # ✅ Ensure candidate_id is a valid integer before querying
        try:
            candidate = get_object_or_404(Candidate, id=int(candidate_id))
        except ValueError:
            messages.error(request, "❌ Invalid candidate selection!")
            return redirect("vote")

        # ✅ Save the vote
        vote = Vote.objects.create(candidate=candidate, user=request.user)
        print(f"✅ Vote Recorded: {vote}")

        messages.success(request, "✅ Your vote has been recorded successfully!")
        return redirect("result")

    return render(request, "vote.html", {"candidates": candidates})
    
# ✅ Logout Page
def logout_view(request):
    logout(request)
    messages.success(request, "✅ You have been logged out!")
    return redirect("login")

# ✅ Result Page
def result(request):
    total_votes = Vote.objects.count()
    winner = Candidate.objects.annotate(_total_votes=Count("vote")).order_by("-_total_votes").first()

    vote_percentage = (winner._total_votes / total_votes) * 100 if winner and total_votes > 0 else 0

    context = {
        "winner_name": winner.name if winner else "No Winner",
        "winner_votes": winner._total_votes if winner else 0,
        "vote_percentage": f"{vote_percentage:.2f}%" if winner else "0.00%",
    }
    return render(request, "results.html", context)

# ✅ Dashboard View
@login_required(redirect_field_name=None)
def dashboard_view(request):
    return render(request, "dashboard.html")

