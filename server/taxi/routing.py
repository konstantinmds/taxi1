from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter

from trips.consumers import TaxiConsumer
from taxi.middleware import TokenAuthMiddlewareStack

application = ProtocolTypeRouter({
  'websocket': TokenAuthMiddlewareStack (
    URLRouter([
      path('taxi/', TaxiConsumer),
  ]),
  ),
}) 
