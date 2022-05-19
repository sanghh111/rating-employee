from api.serializers import BasicSerializer, serializers
from api.user.serializers import UserSerializer
from api.group_skill.serializers import GroupSkillSerializer


class DocxImportSerializer(BasicSerializer):

    header = serializers.IntegerField()
    user = UserSerializer()
        
