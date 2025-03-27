from django.contrib import admin  
from django.db.models import Count, F, FloatField, Max  
from django.db.models.functions import Cast  
from django.utils.translation import gettext_lazy as _

from home.models import Candidate, Vote  

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    """Admin panel settings for Candidate model."""

    list_display = ("id", "name", "total_votes", "vote_percentage", "is_winner")  # ✅ Added "is_winner"

    def get_queryset(self, request):
        """Modify the queryset to include total votes and vote percentage."""
        queryset = super().get_queryset(request)

        # ✅ Annotate candidates with total votes
        queryset = queryset.annotate(_total_votes=Count("vote"))  

        # ✅ Get total votes in the system
        total_votes = Vote.objects.count()  

        # ✅ Avoid division by zero
        if total_votes > 0:
            queryset = queryset.annotate(
                _vote_percentage=Cast(F("_total_votes") * 100.0 / total_votes, FloatField())
            )
        else:
            queryset = queryset.annotate(_vote_percentage=0.0)

        return queryset  

    def total_votes(self, obj):
        """Return the total votes received by the candidate."""
        return obj._total_votes  

    def vote_percentage(self, obj):
        """Return the percentage of total votes the candidate received."""
        return f"{obj._vote_percentage:.2f}%"

    @admin.display(description="Election Result")  # ✅ Fixed admin error
    def is_winner(self, obj):
        """Return 🏆 if the candidate has the most votes."""
        highest_votes = Candidate.objects.annotate(_total_votes=Count("vote")).aggregate(max_votes=Max("_total_votes"))["max_votes"] or 0
        return "🏆 Winner" if obj._total_votes == highest_votes else "❌ Lost"

    # ✅ Enable sorting in admin panel
    total_votes.admin_order_field = "_total_votes"
    total_votes.short_description = "Total Votes"

    vote_percentage.admin_order_field = "_vote_percentage"
    vote_percentage.short_description = "Vote %"

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    """Admin panel settings for Vote model."""
    
    list_display = ("id", "user", "candidate", "timestamp")  # ✅ Show essential fields
    ordering = ("-timestamp",)  # ✅ Show latest votes first
    actions = ["bulk_delete_votes", "reset_all_votes"]  # ✅ Register bulk actions

    def bulk_delete_votes(self, request, queryset):
        """✅ Bulk delete selected votes."""
        count = queryset.count()  # Count how many votes are selected
        queryset.delete()  # Delete selected votes
        self.message_user(request, _(f"Successfully deleted {count} votes."))  

    bulk_delete_votes.short_description = "❌ Bulk Delete Selected Votes"

    def reset_all_votes(self, request, queryset):
        """✅ Reset all votes in the system."""
        Vote.objects.all().delete()  # Delete all votes
        self.message_user(request, _("✅ All votes have been reset."))  

    reset_all_votes.short_description = "🔄 Reset All Votes"