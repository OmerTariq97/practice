import os, django, environ

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "coresite.settings")
django.setup()

env = environ.Env()
environ.Env.read_env()


test = env('TEST')

print(test)
file_object = open('filters', 'r')
for line in file_object:
    print(line)