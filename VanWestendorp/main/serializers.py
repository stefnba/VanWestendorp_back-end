from rest_framework import serializers

from .models import Input_Answer, Input_Title, Input_User, Question, Project

from decimal import Decimal


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'




"  "
class InputAnswersSerializer(serializers.ModelSerializer):      
    class Meta:
        model = Input_Answer
        fields = '__all__'

" Save input, answers with M2M to database "
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

" Nested input fields for QuestionListSerializer "
class InputTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input_Title
        fields = ('__all__')

" List all questions with nested input fields "
class QuestionListSerializer(serializers.ModelSerializer):      
    input_title = InputTitleSerializer(many=True, read_only=True)
    input_count = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'question', 'rank', 'category', 'type', 'input_prefix', 'input_suffix', 'input_count', 'input_title')

    # Serializer Method Field to count number of input fields associated with question
    def get_input_count(self, obj):
        return obj.input_title.count()


"  "
class AnswersOutputSerializer(serializers.ModelSerializer):      
    class Meta:
        model = Input_Answer
        fields = ('input',)
    def to_representation(self, instance):
            self._instance = instance
            # print(instance.input)
            return {'x': instance.input, 'y': '2wkf'}


" List all input fields with associated answers (reverse relation) "
class InputListSerializer(serializers.ModelSerializer):
    # input = AnswersOutputSerializer(many=True, read_only=True)
    
    class Meta:
        model = Input_Title
        fields = ('id', 'title',)

    def to_representation(self, instance):
            # get data for serializer instance
            data = super(InputListSerializer, self).to_representation(instance)

            print(instance)

            answers = []
            # get alls answers for given input fields and sort
            if instance.vw_type.id in [1, 2]: 
                answers = instance.input.all().order_by('-input').values('input')
            if instance.vw_type.id in [3, 4]:
                answers = instance.input.all().order_by('input').values('input')

            # counter for cum distribution
            counter = 0
            # scatter shell for x and y 
            scatters = []
            # decimals for rounding cum distribution
            decimal_rounding = 6
            
            for answer in answers:
                scatters.append({
                    'x': answer['input'],
                    'y': round(Decimal((counter+1) / answers.count()), decimal_rounding) # cumulative distribution
                })
                counter = counter + 1         

            data['input'] = scatters
            return data

" Retrieve single question with all input fields and answers -> output "
class OutputQuestionSerializer(serializers.ModelSerializer):
    input_title = InputListSerializer(many=True)
    
    class Meta:
        model = Question
        fields = ('id', 'question', 'project', 'rank', 'type', 'input_suffix', 'input_prefix', 'input_title', )
        depth = 1
    
    # def to_representation(self, instance):
    #         # get data for serializer instance
    #         data = super(OutputQuestionSerializer, self).to_representation(instance)
    #         # i = instance.input_title.all()
    #         # data['input_title'] = {
    #         #     'df': 2
    #         # }
    #         return data