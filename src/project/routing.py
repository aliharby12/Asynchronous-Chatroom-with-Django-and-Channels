from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

# this application for routes of channels
# it's equal to urlpatterns in the default routes
application = ProtocolTypeRouter({

    # define the authmiddleware to fetch the authenticated user
    'websocket' : AuthMiddlewareStack(

        #define the routes
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
})