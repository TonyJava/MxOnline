# _*_ coding:utf-8 _*_
__author__ = 'bobby'
__date__ = '2017/5/18 10:15'

from django.conf.urls import url

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoPlayView
urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    # 视频列表页
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),
    # 课程评论
    url(r'^comments/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comment'),
    #  添加评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),
    #  添加课程视频
    url(r'^add_comment/$', VideoPlayView.as_view(), name='video_play'),

]