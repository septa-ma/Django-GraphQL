import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Posts

# graphql represents DB as a graph structure
# what does 'DjangoObjectType' do for us?
# Graphene needs to know about each type of object which 
# will appear in the graph.
# To create GraphQL types for each of our Django models, 
# we are going to subclass the DjangoObjectType class which will
# automatically define GraphQL fields that correspond to the 
# fields on the Django models.
# 1- select data we want to use in our schema.
class PostsType(DjangoObjectType): 
    class Meta:
        model = Posts
        # If you only want a subset of fields to be present, 
        # you can use fields or exclude.
        fields = ("id", "title", "description")

# define query and resolver.
# we will list those types as fields in the Query class.
# For each Field in our Schema, we write a Resolver method to 
# fetch data requested by a client’s Query using the current 
# context and Arguments
 # 2- create query class.
class Query(graphene.ObjectType):
    all_posts = graphene.List(PostsType)
    # 3- write the query want to run on our data.
    def resolve_all_posts(root, info):
        return Posts.objects.all()

# for more complex input can use InputObjectType.
class PostInput(graphene.InputObjectType):
    title = graphene.String(required=True)
    description = graphene.String(required=True)

class CreatePost(graphene.Mutation):
    # define the input paramaters for mutation
    class Arguments:
        post_data = PostInput(required=True)
    # define the response of the mutation
    created = graphene.Boolean()
    new_post = graphene.Field(PostsType)
    # mutate is the function that will be applied once 
    # the mutation is called.
    @classmethod
    def mutate(cls, root, info, post_data=None):
        new_post = Posts(title=post_data.title, description=post_data.description)
        new_post.save()
        created = True
        return CreatePost(new_post=new_post, created=created)

class UpdatePost(graphene.Mutation):
    # define the input paramaters for mutation
    class Arguments:
        id = graphene.ID()
        post_data = PostInput(required=True)
    # define the response of the mutation
    updated = graphene.Boolean()
    update_post = graphene.Field(PostsType)
    # mutate is the function that will be applied once 
    # the mutation is called.
    @classmethod
    def mutate(cls, root, info, id, post_data=None):
        update_post = Posts.objects.get(id=id)
        update_post.title = post_data.title
        update_post.description=post_data.description
        update_post.save()
        updated = True
        return UpdatePost(update_post=update_post, updated=updated)

class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    deleted = graphene.Boolean()
    delete_post = graphene.Field(PostsType)

    @classmethod
    def mutate(cls, root, info, id):
        delete_post = Posts.objects.get(id=id)
        delete_post.delete()
        deleted = True
        return DeletePost(deleted=deleted)

# all mutations of graph come here.
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation) 