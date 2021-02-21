"""Defines URL patterns for learnings_logs."""

from django.urls import path
from . import views

urlpatterns = [
  # Home page
  path('', views.index, name='index'),

  # Show all topics
  path('topics/', views.topics, name='topics'),

  # Detail page for a single topic
  path('topics/<topic_id>', views.topic, name='topic'),
]