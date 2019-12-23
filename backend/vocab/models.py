from django.db import models

# Create your models here.

class Learner(models.Model):
    username = models.CharField(max_length=100)


class VocabItem(models.Model):
    text = models.TextField()
    language = models.TextField()
    meaning = models.TextField()
    morphology = models.TextField(null=True)
    pronunciation = models.TextField(null=True)
    category = models.TextField(null=True)
    subcategory = models.TextField(null=True)
    source = models.TextField(null=True)
    last_practiced = models.DateTimeField(null=True)

    def __str__(self):
        return self.text


class VocabList(models.Model):
    vocab_items = models.ManyToManyField(VocabItem)
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)


class Microblog(models.Model):
    text = models.TextField()
    language = models.TextField()
    learner = models.ForeignKey(Learner, on_delete=models.CASCADE)
