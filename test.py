from faker import Faker
from faker_nonbinary import Provider as NonbinaryProvider

fake = Faker()
fake.add_provider(NonbinaryProvider)
print(fake.real_name_nonbinary())
