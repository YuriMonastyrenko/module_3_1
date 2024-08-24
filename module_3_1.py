calls = 0
def  count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    output = (len(string), string.upper(), string.lower())
    print(output)

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [s.lower() for s in list_to_search]
    print(string in list_to_search)

string_info("cAr")
string_info("Coconut")
is_contains("BaNaNA", ["CHerrY", "Mango", "MeLON"])
is_contains("LadA", ["VaZ", "VOlGa", "BuGaTTi","laDA"])
print(calls)









