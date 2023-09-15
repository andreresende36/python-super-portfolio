from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

user = User.objects.get(
    username="andreresende"
)  # Substitua 'seu_usuario' pelo nome de usuário desejado
refresh = RefreshToken.for_user(user)

# Token de acesso (válido por um curto período de tempo)
access_token = str(refresh.access_token)  # type: ignore

print(f"Token de Acesso: {access_token}")
