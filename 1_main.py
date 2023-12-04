
def dzielenie(x,y):
    if y == 0:
        raise ZeroDivisionError("Dzielenie przez 0") #rzucanie istniejacego wyjątku. W nawiasie podany argument to komunikat jaki chcemy podać użytkownikowi
    print(x/y)

# wywolanie takiej funkcji rzuci Nam zdefiniowany wyjatek
# dzielenie(2,0)

# probujac to obsluzyc try except uda Nam się to obsluzyc
try:
    dzielenie(2,0)
except ZeroDivisionError:
    print("Nie możesz dzielić przez 0")

#podanie wyjątku jeszcze dalej do obsługi przy uzyciu raise
# try:
#     dzielenie(2,0)
# except ZeroDivisionError:
#     print("Nie możesz dzielić przez 0")
#     raise

print("-------------")
#Asercja
# podobne do if raise error
def dzielenie(x,y):
    # przyjmuje warunek, przerywa program kiedy nie jest spełniony
    assert y != 0, " Y == 0" # krótki opis opcjonalnie jako drugi argument
    print(x/y)

dzielenie(3, 1)
# dzielenie(3, 0)


print("--------")
#kompleksowy przykład użycia raise, try, except
def divide(a,b):
    if(b == 0):
        raise ZeroDivisionError("Dzielnik musi być różny od zera")
    return a/b

try:
    r = divide(4,0)
    print(r)
except ZeroDivisionError:
    print("Nie można dzielić przez zero")


