from django.http import Http404
from django.views.generic import ListView, DetailView, UpdateView

# from django.http import Http404
# from django.shortcuts import render
from . import models

# Create your views here.


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwargs = "potato"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room
    pk_url_kwarg = "pk"


# def room_detail(request, pk):

#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(
#             request,
#             "rooms/detail.html",
#             context={
#                 "room": room,
#             },
#         )
#     except models.Room.DoesNotExist:
#         raise Http404()


class EditRoomView(UpdateView):
    model = models.Room
    template_name = "rooms/room_edit.html"
    fields = (
        "name",
        "description",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
    )

    def get_object(self, queryset=None):
        room = super().get_object(queryset=queryset)
        if room.host.pk != self.request.user.pk:
            raise Http404()
        return room
