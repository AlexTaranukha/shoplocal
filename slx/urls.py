# Package imports
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns

# Shoplocal imports
from slx import views


handler404 = views.four_o_four_error_view
handler500 = views.five_hundred_error_view

urlpatterns = staticfiles_urlpatterns()
urlpatterns += format_suffix_patterns(patterns('slx.views',
    url(r'^api/affiliations/$', views.AffiliationList.as_view(), name='affiliation-list'),
    url(r'^api/affiliations/(?P<pk>\d+)/$', views.AffiliationInstance.as_view(), name='affiliation-instance'),
    url(r'^api/asks/$', views.AskList.as_view(), name='ask-list'),
    url(r'^api/asks/(?P<pk>\d+)/$', views.AskInstance.as_view(), name='ask-instance'),
    url(r'^api/bids/$', views.BidList.as_view(), name='bid-list'),
    url(r'^api/bids/(?P<pk>\d+)/$', views.BidInstance.as_view(), name='bid-instance'),
    #url(r'^api/fulfillments/$', views.FulfillmentList.as_view(), name='fulfillment-list'),
    #url(r'^api/fulfillments/(?P<pk>\d+)/$', views.FulfillmentInstance.as_view(), name='fulfillment-instance'),
    url(r'^api/placements/$', views.PlacementList.as_view(), name='placement-list'),
    url(r'^api/placements/(?P<pk>\d+)/$', views.PlacementInstance.as_view(), name='placement-instance'),
    url(r'^api/statuses/$', views.StatusList.as_view(), name='status-list'),
    url(r'^api/statuses/(?P<pk>\d+)/$', views.StatusInstance.as_view(), name='status-instance'),
    url(r'^api/units/$', views.UnitList.as_view(), name='unit-list'),
    url(r'^api/units/(?P<pk>\d+)/$', views.UnitInstance.as_view(), name='unit-instance'),
    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>\d+)/$', views.UserInstance.as_view(), name='user-instance'),
))

