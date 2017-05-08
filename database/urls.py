from django.conf.urls import url
from database import views


urlpatterns = [
    # ---- stores all the listings ---- # 
    url(r'^user/$',views.UserList.as_view()),
    url(r'^counselor/$',views.CounselorList.as_view()),
    url(r'^conversation/$',views.ConversationList.as_view()),

    # ---- entries for search ----- #
        # Note this regex looks for UUID of hex with: 8 - 4 - 4 - 4 - 12 pattern
    url(r'^user/(?P<gliaID>[0-9a-f]{8}-([0-9a-f]{4}-){3}[0-9a-f]{12})/$',views.UserDetail.as_view()),
    url(r'^counselor/(?P<pk>[0-9]+)/$',views.CounselorDetail.as_view()),
    url(r'^conversation/(?P<conversationID>[0-9]+)/$',views.ConversationDetail.as_view()),

    # ---- statistics endpoints ---- #
    url('^statistics/$', views.Statistics.as_view()),
]