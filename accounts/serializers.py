from rest_framework.serializers import ModelSerializer
from .models import MyUser



class MyUserSerializer(ModelSerializer):

    class Meta:
        model = MyUser
        fields = "__all__"
        
class MyUserSerializerPOST(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email','password','name','img_perfil']

    def create(self, validate_data):
        user = super().create(validated_data=validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user
    

class MyUserSerializerUpdate(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password', 'name', 'img_perfil']

    def update(self, instance, validated_data):
        # Actualiza los campos de la instancia con los datos validados
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.img_perfil = validated_data.get('img_perfil', instance.img_perfil)

        # Actualiza la contraseña si se proporciona una nueva
        new_password = validated_data.get('password')
        if new_password:
            instance.set_password(new_password)

        # Guarda los cambios en la instancia
        instance.save()
        return instance
