import graphene
from pages.schema import Query as music_query

class Query(music_query):
    pass


schema = graphene.Schema(query=Query)