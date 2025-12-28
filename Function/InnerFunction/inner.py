def function1(msg):
    def function2():
        print(msg)
    function2()
function1("Hello,World!")