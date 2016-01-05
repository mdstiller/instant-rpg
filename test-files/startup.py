loader = template.Loader("/home/btaylor")
print loader.load("template_test.html").generate()