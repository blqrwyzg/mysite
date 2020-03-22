import datetime
from haystack import indexes
from .models import article

class articleIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)


    def get_model(self):
        return article

    def index_queryset(self, using=None):
        return self.get_model().article_release.all()