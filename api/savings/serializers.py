from rest_framework import serializers

from savings.models import Savings, Days, Numbers

class DaysSerializer(serializers.ModelSerializer):

	class Meta:
		model = Days
		fields = ['n_days']

class NumbersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Numbers
		fields = ['numeros']

class SavingsSerializer(serializers.ModelSerializer):
	numbers = NumbersSerializer(many=True)

	class Meta:
		model = Savings
		fields = ['user', 'days', 'numbers']

	def create(self, validated_data):
		numbers = validated_data.pop('numbers')
		savings = Savings.objects.create(**validated_data)
		for dato in numbers:
			n = Numbers.objects.create(numeros=dato["numeros"])
			savings.numbers.add(n)
		return savings
