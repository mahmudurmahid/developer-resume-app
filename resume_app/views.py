from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Resume, JobDescription
from .serializers import ResumeSerializer, JobDescriptionSerializer

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page"
    """
    template_name = 'index.html'

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_resume(request):
    """
    Handle resume file uploads.
    """
    file = request.FILES.get('file')
    
    if not file:
        return Response({"error": "No file provided."}, status=400)

    if not file.name.endswith(('.pdf', '.docx', '.txt')):
        return Response({"error": "Invalid file format. Please upload a PDF, DOCX, or TXT file."}, status=400)

    resume = Resume.objects.create(user=request.user, file=file)
    return Response({"message": "Resume uploaded successfully.", "resume_id": resume.id})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_job_description(request):
    """
    Handle job description submission.
    """
    serializer = JobDescriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=400)