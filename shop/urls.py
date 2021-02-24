from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productView, name="ProductView"),
    path("test", views.test, name="test"),
    path("testex", views.testex, name="testex"),
    path("prodView/<int:id>/", views.prodView, name="ProductView"),
    path("aboutus", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("checkout", views.checkout, name="checkout"),

]

