from rest_framework import serializers
from products.models import Product, ProductReview, ProductApprovalStatusChoices, ProductReviewApprovalStatusChoices

# Product Serializer using ModelSerializer to automatically generate a set of fields based on Product model
class ProductSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(format='%d/%m/%y %H:%M')

    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['created_by'] = {"username":instance.created_by.username, "email": instance.created_by.email}
        except:
            representation['created_by'] = {"username": "", "email": ""}
        return representation

# Product Detail Serializer using the below fields
class ProductDetailSerializer(serializers.ModelSerializer):
    user_reviews = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    total_reviews_count = serializers.SerializerMethodField()
    reviews_percentage = serializers.SerializerMethodField()
    graph_circle = serializers.SerializerMethodField()

    def get_average_rating(self, obj):
        # average of review
        reviews = ProductReview.objects.filter(product=obj, approval_status=ProductReviewApprovalStatusChoices.APPROVED)
        total_rating = 0
        if reviews.count() > 0:
            for review in reviews:
                total_rating += review.rating
            return round(total_rating / reviews.count(),2)
        else:
            return 0

    def get_graph_circle(self, obj):
        reviews = ProductReview.objects.filter(product=obj, approval_status=ProductReviewApprovalStatusChoices.APPROVED)
        if reviews is None:
            return 0
        total_rating = 0
        if reviews.count() > 0:
            for review in reviews:
                total_rating += review.rating
            total_rating = round(total_rating / reviews.count(), 2)
            percentage = (total_rating*100)/5
            return int(180*percentage)/100
        else:
            return 0

    def get_total_reviews(self, obj):
        total_count = ProductReview.objects.filter(product=obj, approval_status=ProductReviewApprovalStatusChoices.APPROVED).count()
        if total_count == 0:
            return 0
        review_list = {
            "one_star_count": round((ProductReview.objects.filter(product=obj, rating=1, approval_status=ProductReviewApprovalStatusChoices.APPROVED).count()*100)/total_count,2),
            "two_star_count": round((ProductReview.objects.filter(product=obj, rating=2, approval_status=ProductReviewApprovalStatusChoices.APPROVED).count()*100)/total_count,2),
            "three_star_count": round((ProductReview.objects.filter(product=obj, rating=3, approval_status=ProductReviewApprovalStatusChoices.APPROVED).count()*100)/total_count,2),
            "four_star_count": round((ProductReview.objects.filter(product=obj, rating=4, approval_status=ProductReviewApprovalStatusChoices.APPROVED).count()*100)/total_count,2),
            "five_star_count": round((ProductReview.objects.filter(product=obj, rating=5, approval_status=ProductReviewApprovalStatusChoices.APPROVED).count()*100)/total_count,2),
        }

        return review_list

    def get_user_reviews(self, obj):
        reviews = ProductReview.objects.filter(product=obj, approval_status=ProductReviewApprovalStatusChoices.APPROVED)
        review_list = list()
        for review in reviews:
            review_list.append(
                {
                    "username": review.review_by.username,
                    "full_name": review.review_by.first_name + review.review_by.last_name,
                    "skill_level": review.review_by.skill_level,
                    "location": review.review_by.location,
                    "category": review.category,
                    "session": review.session,
                    "comment": review.comment,
                    "rating": review.rating,
                    "profile_image": str(review.review_by.profile_image) if review.review_by.profile_image else "",
                    "date": review.get_date()
                }
            )
        return review_list

    def get_total_reviews_count(self, obj):
        return ProductReview.objects.filter(product=obj, approval_status=ProductReviewApprovalStatusChoices.APPROVED).count()

    def get_reviews_percentage(self, obj):
        reviews = ProductReview.objects.filter(product=obj, approval_status=ProductReviewApprovalStatusChoices.APPROVED)
        if reviews is None:
            return 0
        total_rating = 0
        if reviews.count() > 0:
            for review in reviews:
                total_rating += review.rating
            total_rating = round(total_rating / reviews.count(), 2)
            return (total_rating*100)/5
        else:
            return 0

    class Meta:
        model = Product
        fields = '__all__'

# Product Review Serializer using ModelSerializer
class ProductReviewSerializer(serializers.ModelSerializer):
    review_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    created_at = serializers.DateTimeField(format='%d/%m/%y %H:%M')


    class Meta:
        model = ProductReview
        fields = '__all__'
        read_only_fields = ('created_by',)
        extra_kwargs = {
            'product': {'required': True},
            'rating': {'required': True},
            'comment': {'required': True},
        }

    def create(self, validated_data):
        return ProductReview.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.save()
        return instance

    def validate(self, data):
        if data['rating'] < 1 or data['rating'] > 5:
            raise serializers.ValidationError("Rating should be between 1 and 5")
        return data

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value

    def validate_product_id(self, value):
        if not Product.objects.filter(id=value).exists():
            raise serializers.ValidationError("Product does not exist")
        return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        try:
            representation['username'] = instance.review_by.username
        except:
            representation['username'] = ""
        return representation
