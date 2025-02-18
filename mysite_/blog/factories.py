import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

faker = FakerFactory.create() # Create a faker instance


class UserFactory(factory.django.DjangoModelFactory): # Create a UserFactory class
    class Meta:
        model = User

    email = factory.Faker("safe_email") # Use faker to generate an email
    username = factory.LazyAttribute(lambda x: faker.name()) # Use faker to generate a name


    @classmethod
    def _prepare(cls, create, **kwargs): # Prepare the user
        password = kwargs.pop("password", None) # Pop the password from the kwargs
        user = super(UserFactory, cls)._prepare(create, **kwargs) #prepare the user
        if password:
            user.set_password(password)
            if create:
                user.save()
            return user
        
class PostFactory(factory.django.DjangoModelFactory): # Create a PostFactory class
    title = factory.LazyAttribute(lambda x: faker.sentence()) # Use faker to generate a sentence
    created_on = factory.LazyAttribute(lambda x: now()) # Use the current time
    author = factory.SubFactory(UserFactory) # Use the UserFactory to create an author
    status = 0


    class Meta:
        model = Post # The model to Post