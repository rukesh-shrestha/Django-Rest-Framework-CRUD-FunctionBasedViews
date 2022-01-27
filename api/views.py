from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializers
from .models import Tasks
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def tasks(request):
    tasks = Tasks.objects.all()
    serializer = TaskSerializers(tasks,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def detailtask(request,pk):
    task = Tasks.objects.get(id=pk)
    serializer = TaskSerializers(task,many=False)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def posttask(request):
    serializer = TaskSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"Data" : "Formate Invalid"})
    return Response({"Data":"Save successfully!!!"},status=status.HTTP_201_CREATED)


@api_view((['PUT']))
def updatetask(request,pk):
    task = Tasks.objects.get(id=pk)
    serializer = TaskSerializers(instance=task,data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"Data" : "Formate Invalid"})
    return Response({"Data":"Update successfully!!!"},status=status.HTTP_201_CREATED)

@api_view((['DELETE']))
def deletetask(request,pk):
    if(Tasks.objects.get(id=pk)):
        task = Tasks.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)




