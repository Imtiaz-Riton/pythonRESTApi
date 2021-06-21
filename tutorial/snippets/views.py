from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet, ModelToDelete
from snippets.serializers import SnippetSerializer, ModelToDeleteSerializer
from django.shortcuts import get_object_or_404
from .get_model_name import get_model_name
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView


class SnippetList(APIView):

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):

    def get_object(self, pk):

        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):

        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):

        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModelList(APIView):

    def get(self, request, format=None):
        model_list = ModelToDelete.objects.all()
        serializer = ModelToDeleteSerializer(model_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #data = JSONParser().parse(request)
        serializer = ModelToDeleteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=404)


@csrf_exempt
def snippet_detail(request, pk):

    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(Snippet, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=404)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse(status=204)

@api_view(['GET','POST'])
def model_to_delete_list(request):
    if request.method == 'GET':
        modeltolist = ModelToDelete.objects.all()
        serializer = ModelToDeleteSerializer(modeltolist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ModelToDeleteSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

        return JsonResponse(serializer.errors, status=404)

"""
@api_view(['POST'])
def model_delete(request, pk):

    if request.method == 'POST':
        data = JSONParser().parse(request)
        name = data['name']
        model_name = get_model_name(name)
        snippet = get_object_or_404(model_name, pk=pk)
        snippet.delete()
        return Response(status=204)

class ModelDelete(APIView):

    def post(self, request, pk, format=None):
        name = request.data['name']
        model_name = get_model_name(name)
        snippet = get_object_or_404(model_name, pk=pk)
        snippet.delete()
        return Response(status=204)