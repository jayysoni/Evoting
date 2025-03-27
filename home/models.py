from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# ✅ Vote Model - Stores votes from users
class Vote(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # ✅ One vote per user
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)  # ✅ Prevents candidate deletion if votes exist
    timestamp = models.DateTimeField(auto_now_add=True)  # ✅ Stores the time of the vote

    class Meta:
        verbose_name = "Vote"
        verbose_name_plural = "Votes"
        ordering = ["-timestamp"]  # ✅ Newest votes appear first

    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.name}"