# Django-GraphQL
**in this project we build a CRUD operations with GraphQL.**

**App Data Requirements:**
- real-time collaboration
- offline programming model with sync
- get only the data you nees
- fine-grained access control
- flexible DB options
    - REST has weeknees in this item.

**REST representational state transfer:**
- standard for designning web APIs 
- it's simple to build 
- structured access to resources

**what are the weeknesses of REST-Framework?**
- inflexible to rapid changing requirements
- over fetching
    - when the client downloads more informations that
    is actually required.
- under fetching
    - a specific end-point doesn't provide enough of the 
    required information.

# what is GraphQL?
- is an API standard
- provides efficiency, flexibility
- was designed to fix many of the problems that we found of RESTful architecture
- is a data query language
- represent DB as a graph structure

**what are the advantages of GraphQL?**
- fetching data with queries:
    - query {
        - posts { **the model name**
            - title **specific fields want to collect**
            - author { 
                - name
                - age
             }
         }
     }
- exposess a single endpoint
- responds with precise data from client requests
- enables declarative data fetching
    - multiple endpoints that return fixed data structures

# working with GraphQL:
- make the project and app
- define a model in app/models.py
- graphene is required for graphql
    - **a library that provides tools to implement graphql api in python**
    - pip install graphene-django
    - add 'graphene_django' at projectname/settings.py in INSTALLED_APPS list
    - add this dictionary at projectname/settings.py
        - GRAPHENE = {
            - 'SCHEMA': 'app.schema.schema'
        - }
    - set up a GraphQL endpoint in our Django app in appname/urls.py add these also we can declare schema in urls.py add 'schema=schema' in url[]:
        - from graphene_django.views import GraphQLView
        - urlpatterns = [
            - url(r'^graphql$', GraphQLView.as_view(graphiql=True)),
        - ]
- inside app folder make schema.py
    - a graphQL schema defines the types and relationships between fields in your API.
    - in schema, describe our data models that we are going to provide to the GraphQL server, and all the oprations we can then perform on that data.
        - it is like serializer in REST, the difference is in serializer all the data we collect on the fields send back, but here we build queries and can define what kind of data want to be returned.
        - **Mutation -> for saveing data in DB.**
        - **Query -> for reading data from DB.**