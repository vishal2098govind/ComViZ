from Compiler.run import run

while True:
    text = input('comviz >')
    result, error = run('<stdin>', text)
    if error:
        print(error.as_string())
    else:
        print(result)
