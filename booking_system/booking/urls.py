from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, BookingViewSet, AvailabilityViewSet, BookingFormView

router = DefaultRouter()
router.register('rooms', RoomViewSet)
router.register('bookings', BookingViewSet)
router.register('availability', AvailabilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('book/', BookingFormView.as_view(), name='booking_form')
]