def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments (tuple):", args)
    print("Keyword arguments (dictionary):", kwargs)


my_function("User Info", "Emil", "Tobias", age=25, city="Oslo")
