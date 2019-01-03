import os

def populate():
    python_cat = add_cat("Python", views=0, likes=64)
    add_page(cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/")
    add_page(cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/")
    add_page(cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django", views=64, likes=32)
    add_page(cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/")
    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks", views=32, likes=16)
    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/")
    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org")
    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            #{0} and {1} is mapped with .format, first arg in format is 0, then 1
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    # use position [0] because get_or_create will return a tuple of (object, created) where created
    # is a bool of True when object created
    updated_values = {'views': cat.views}
    p = Page.objects.update_or_create(category=cat, title=title, url=url, defaults=updated_values)[0]
    return p


def add_cat(name, views, likes):
    updated_values = {'views': views, 'likes': likes}
    c = Category.objects.update_or_create(
        name=name,
        defaults=updated_values,
    )[0]
    return c

#execution starts here
if __name__ == '__main__':
    print("Starting Rango population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    print("Loading Tango with Django Project Settings...")

    # If running as standalone script, must import and setup django.
    import django
    print("Importing Django...")
    django.setup()
    print("Setting up Django...")

    # cannot call rango app until settings have been established
    from rango.models import Category, Page
    print("Loading rango.models")
    populate()
