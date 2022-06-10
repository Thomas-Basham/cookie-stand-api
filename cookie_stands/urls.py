from django.urls import path
from views import CookieStandList, CookieStandDetail, CookieStandListView

urlpatterns = [
    path("", CookieStandListView.as_view(), name="cookie_stand_list"),
    path("api/admin/", CookieStandList.as_view(), name="cookie_stand_list_api"),
    path("api/admin/<int:pk>/", CookieStandDetail.as_view(), name="cookie_stand_detail"),
]
