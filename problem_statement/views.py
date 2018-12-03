# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Contests, Colleges, Challenges, View_Stats, Submission_Stats, Result_Stats
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework import renderers
from rest_framework.views import APIView
from rest_framework.response import Response

# # Serializers define the API representation.
class ContestSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = Contests
        fields = ('contest_id', 'hacker_id', 'name')

class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = Colleges
        fields = ('contest_id', 'college_id')
class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = Challenges
        fields = ('college_id', 'challenges_id', )
        # """docstring for  Meta:"""
        # def __init__(self, arg):
        #   super( Meta:, self).__init__()
        #   self.arg = arg
class ViewStatsSerializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = View_Stats
        fields = ('challenges_id', 'total_views', 'total_uniqueviews', )

class Submission_Stats_Serializer(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model = Submission_Stats
        fields = ('challenges_id', 'total_accept_submission', 'total_submission')
            
class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result_Stats
        fields = ('contest_id', 'name', 'hacker_id', 'total_views','total_uniqueviews','total_submission','total_accept_submission')

# ViewSets define the view behavior.
class ContestViewSet(viewsets.ModelViewSet):    
    queryset = Contests.objects.all()
    print "$$$", queryset
    serializer_class = ContestSerializer
class ProblemViewSet(viewsets.ModelViewSet):
    # renderer_classes = [TemplateHTMLRenderer]    
    queryset1 = Contests.objects.filter(contest_id="94828")
    contest_id = 0
    hacker_id = 0
    name = ""
    for i in queryset1:
        contest_id = i.contest_id
        name = i.name
        hacker_id = i.hacker_id
    queryset2 = Colleges.objects.filter(contest_id="94828")
    clg_id = 0
    for i in queryset2:
        clg_id = i.college_id
    queryset3 = Challenges.objects.filter(college_id=clg_id)
    li = []
    for j in queryset3:
        li.append(j.challenges_id)
    # print "$$$$$$$$", li

    queryset5 = View_Stats.objects.filter(challenges_id__in=li)

    total_views = 0
    total_uniqueviews = 0
    for dd in queryset5:
        total_views+=int(dd.total_views)
        total_uniqueviews+=int(dd.total_uniqueviews)

    queryset4 = Submission_Stats.objects.filter(challenges_id__in=li)
    total_accept_submissions = 0
    total_submissionss = 0
    for dd in queryset4:
        total_submissionss+=int(dd.total_submission)
        total_accept_submissions+=int(dd.total_accept_submission)

    # print "$$$", queryset

    print hacker_id
    print contest_id
    print name

    print "###"*30
    print total_views
    print total_uniqueviews
    print "###"*30
    print total_accept_submissions
    print total_submissionss
    result = Result_Stats.objects.filter(contest_id=contest_id)
    if result:
        Result_Stats.objects.filter(contest_id=contest_id).update(contest_id=contest_id, name=name, hacker_id=hacker_id, total_views=total_views,total_uniqueviews=total_uniqueviews,total_submission=total_submissionss,total_accept_submission=total_accept_submissions)
    else:
        Result_Stats.objects.create(contest_id=contest_id, name=name, hacker_id=hacker_id, total_views=total_views,total_uniqueviews=total_uniqueviews,total_submission=total_submissionss,total_accept_submission=total_accept_submissions)

    queryset = Result_Stats.objects.all()
    serializer_class = ResultSerializer
    
    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)
    # return Response({'data':queryset}, template_name="output.html")
    # def list(self, request, *args, **kwargs):
    #     # response = super(ProblemViewSet, self).list(request, *args, **kwargs)
    #     response = ViewStatsSerializer
    #     if request.accepted_renderer.format == 'html':
    #         return Response({'data': response.data}, template_name='output.html')
    #     return response

# class ProblemViewSet(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'output.html'

#     def get(self, request):
#         # queryset = Profile.objects.all()
#         queryset1 = Contests.objects.filter(contest_id="66406")
#         queryset2 = Colleges.objects.filter(contest_id="66406")
#         clg_id = 0
#         for i in queryset2:
#             clg_id = i.college_id
#         queryset3 = Challenges.objects.filter(college_id=clg_id)
#         li = []
#         for j in queryset3:
#             li.append(j.challenges_id)       

#         queryset = View_Stats.objects.filter(challenges_id__in=li)
#         serializer_class = ViewStatsSerializer
#         return Response({'profiles': queryset})

# from rest_framework.decorators import api_view, renderer_classes
# @api_view(['GET'])
# @renderer_classes((JSONRenderer,))
# def user_count_view(request, format=None):
#     """
#     A view that returns the count of active users in JSON.
#     """
#     queryset1 = Contests.objects.filter(contest_id="66406")
#     queryset2 = Colleges.objects.filter(contest_id="66406")
#     clg_id = 0
#     for i in queryset2:
#         clg_id = i.college_id
#     queryset3 = Challenges.objects.filter(college_id=clg_id)
#     li = []
#     for j in queryset3:
#         li.append(j.challenges_id)
#     print "$$$$$$$$", li

#     queryset = View_Stats.objects.filter(challenges_id__in=li)
#     content = {'user_count': queryset}
#     return Response(content)
