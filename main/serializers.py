from rest_framework import serializers

from .models import Input_Answer, Input_Title, Input_User, Question, Project

class InputAnswersSerializer(serializers.ModelSerializer):      
    class Meta:
        model = Input_Answer
        fields = '__all__'

class InputUserSerializer(serializers.ModelSerializer):
    answer = InputAnswersSerializer(many=True)

    class Meta:
        model = Input_User
        fields = '__all__'
    
    # override create for M2M relationship
    def create(self, validated_data):
        answers = validated_data.pop('answer')
        input_user = Input_User.objects.create(**validated_data)
        for answer in answers:
            input_answer = input_user.answer.create(**answer)
            # i = Input_Answer(**answer)
            # i.save()
            # i.fav.add(input_user)
            # Input_Answer.objects.create(fav=input_user, **answer)
        return input_user

class InputTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input_Title
        fields = ('__all__')



class QuestionsSerializer(serializers.ModelSerializer):      
    input_title = InputTitleSerializer(many=True, read_only=True)
    input_count = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'question', 'rank', 'category', 'type', 'input_prefix', 'input_suffix', 'input_count', 'input_title')

    # Serializer Method Field to count number of input fields associated with question
    def get_input_count(self, obj):
        return obj.input_title.count()

