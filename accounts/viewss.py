from datetime import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser, ProfileCustomUser, CarModel, Address, Reclaim, Notification
from .validators import CustomUserValidator, ProfileCustomUserValidator, CarModelValidator, AddressValidator, \
    ReclaimValidator, NotificationValidator
from .permissions import IsDriverOrBoth, IsPassenger


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
def create_user(request):
    user_data = request.data
    data = {
        'username': 'john_doe',
        'birthdate': '1990-01-01',  # Example date format
    }
    try:
        validator = CustomUserValidator(**user_data)
        validator.dict()
        user = CustomUser.objects.create(
            last_name=validator.last_name,
            first_name=validator.first_name,
            email=validator.email,
            is_superuser=validator.is_superuser,
            is_staff=validator.is_staff,
            is_active=validator.is_active,
            date_joined=validator.date_joined or timezone.now()
        )
        return Response(status=status.HTTP_201_CREATED)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsDriverOrBoth])
def read_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    return Response({
        "last_name": user.last_name,
        "first_name": user.first_name,
        "email": user.email,
        "is_superuser": user.is_superuser,
        "is_staff": user.is_staff,
        "is_active": user.is_active,
        "date_joined": user.date_joined
    })


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_user(request, user_id):
    user_data = request.data
    user = get_object_or_404(CustomUser, pk=user_id)
    try:
        validator = CustomUserValidator(**user_data)
        validator.dict()
        user.last_name = validator.last_name
        user.first_name = validator.first_name
        user.email = validator.email
        user.is_superuser = validator.is_superuser
        user.is_staff = validator.is_staff
        user.is_active = validator.is_active
        user.date_joined = validator.date_joined or user.date_joined
        user.save()
        return Response(status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
def create_profile(request):
    profile_data = request.data
    try:
        validator = ProfileCustomUserValidator(**profile_data)
        validator.dict()
        profile = ProfileCustomUser.objects.create(
            user_id=validator.user,
            avatar=validator.avatar,
            birth_date=validator.birth_date,
            genre=validator.genre,
            phone_number=validator.phone_number,
            num_permis=validator.num_permis,
            role=validator.role,
            category=validator.category,
            date_delivrance=validator.date_delivrance or timezone.now(),
            date_expiration=validator.date_expiration
        )
        return Response(status=status.HTTP_201_CREATED)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsPassenger])
def read_profile(request, profile_id):
    profile = get_object_or_404(ProfileCustomUser, pk=profile_id)
    return Response({
        "user": profile.user_id,
        "avatar": profile.avatar,
        "birth_date": profile.birth_date,
        "genre": profile.genre,
        "phone_number": profile.phone_number,
        "num_permis": profile.num_permis,
        "role": profile.role,
        "category": profile.category,
        "date_delivrance": profile.date_delivrance,
        "date_expiration": profile.date_expiration
    })


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_profile(request, profile_id):
    profile_data = request.data
    profile = get_object_or_404(ProfileCustomUser, pk=profile_id)
    try:
        validator = ProfileCustomUserValidator(**profile_data)
        validator.dict()
        profile.user_id = validator.user
        profile.avatar = validator.avatar
        profile.birth_date = validator.birth_date
        profile.genre = validator.genre
        profile.phone_number = validator.phone_number
        profile.num_permis = validator.num_permis
        profile.role = validator.role
        profile.category = validator.category
        profile.date_delivrance = validator.date_delivrance or profile.date_delivrance
        profile.date_expiration = validator.date_expiration
        profile.save()
        return Response(status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_profile(request, profile_id):
    profile = get_object_or_404(ProfileCustomUser, pk=profile_id)
    profile.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
def create_car(request):
    car_data = request.data
    try:
        validator = CarModelValidator(**car_data)
        validator.dict()
        car = CarModel.objects.create(
            owner_id=validator.owner,
            make=validator.make,
            model=validator.model,
            year=validator.year,
            color=validator.color,
            licence_number=validator.licence_number
        )
        return Response(status=status.HTTP_201_CREATED)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsDriverOrBoth])
def read_car(request, car_id):
    car = get_object_or_404(CarModel, pk=car_id)
    return Response({
        "owner": car.owner_id,
        "make": car.make,
        "model": car.model,
        "year": car.year,
        "color": car.color,
        "licence_number": car.licence_number
    })


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_car(request, car_id):
    car_data = request.data
    car = get_object_or_404(CarModel, pk=car_id)
    try:
        validator = CarModelValidator(**car_data)
        validator.dict()
        car.owner_id = validator.owner
        car.make = validator.make
        car.model = validator.model
        car.year = validator.year
        car.color = validator.color
        car.licence_number = validator.licence_number
        car.save()
        return Response(status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_car(request, car_id):
    car = get_object_or_404(CarModel, pk=car_id)
    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
def create_address(request):
    address_data = request.data
    try:
        validator = AddressValidator(**address_data)
        validator.dict()
        address = Address.objects.create(
            position_name=validator.position_name,
            number=validator.number,
            street=validator.street,
            city=validator.city,
            region=validator.region,
            country=validator.country,
            postal_code=validator.postal_code,
            google_maps=validator.google_maps,
            type_of_address=validator.type_of_address,
            author_id=validator.author
        )
        return Response(status=status.HTTP_201_CREATED)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsPassenger])
def read_address(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    return Response({
        "position_name": address.position_name,
        "number": address.number,
        "street": address.street,
        "city": address.city,
        "region": address.region,
        "country": address.country,
        "postal_code": address.postal_code,
        "google_maps": address.google_maps,
        "type_of_address": address.type_of_address,
        "author": address.author_id
    })


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_address(request, address_id):
    address_data = request.data
    address = get_object_or_404(Address, pk=address_id)
    try:
        validator = AddressValidator(**address_data)
        validator.dict()
        address.position_name = validator.position_name
        address.number = validator.number
        address.street = validator.street
        address.city = validator.city
        address.region = validator.region
        address.country = validator.country
        address.postal_code = validator.postal_code
        address.google_maps = validator.google_maps
        address.type_of_address = validator.type_of_address
        address.author_id = validator.author
        address.save()
        return Response(status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_address(request, address_id):
    address = get_object_or_404(Address, pk=address_id)
    address.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
def create_reclaim(request):
    reclaim_data = request.data
    try:
        validator = ReclaimValidator(**reclaim_data)
        validator.dict()
        reclaim = Reclaim.objects.create(
            owner_id=validator.owner,
            date=validator.date,
            reason=validator.reason
        )
        return Response(status=status.HTTP_201_CREATED)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsPassenger])
def read_reclaim(request, reclaim_id):
    reclaim = get_object_or_404(Reclaim, pk=reclaim_id)
    return Response({
        "owner": reclaim.owner_id,
        "date": reclaim.date,
        "reason": reclaim.reason
    })


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_reclaim(request, reclaim_id):
    reclaim_data = request.data
    reclaim = get_object_or_404(Reclaim, pk=reclaim_id)
    try:
        validator = ReclaimValidator(**reclaim_data)
        validator.dict()
        reclaim.owner_id = validator.owner
        reclaim.date = validator.date
        reclaim.reason = validator.reason
        reclaim.save()
        return Response(status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_reclaim(request, reclaim_id):
    reclaim = get_object_or_404(Reclaim, pk=reclaim_id)
    reclaim.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsDriverOrBoth])
def create_notification(request):
    notification_data = request.data
    try:
        validator = NotificationValidator(**notification_data)
        validator.dict()
        notification = Notification.objects.create(
            sender_id=validator.sender,
            receiver_id=validator.receiver,
            date=validator.date,
            message=validator.message,
            status=validator.status
        )
        return Response(status=status.HTTP_201_CREATED)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsPassenger])
def read_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    return Response({
        "sender": notification.sender_id,
        "receiver": notification.receiver_id,
        "date": notification.date,
        "message": notification.message,
        "status": notification.status
    })


@api_view(['PUT'])
@permission_classes([IsDriverOrBoth])
def update_notification(request, notification_id):
    notification_data = request.data
    notification = get_object_or_404(Notification, pk=notification_id)
    try:
        validator = NotificationValidator(**notification_data)
        validator.dict()
        notification.sender_id = validator.sender
        notification.receiver_id = validator.receiver
        notification.date = validator.date
        notification.message = validator.message
        notification.status = validator.status
        notification.save()
        return Response(status=status.HTTP_200_OK)
    except ValueError as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsDriverOrBoth])
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id)
    notification.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
