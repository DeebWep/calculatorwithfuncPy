print("\t\t\t>>>SADE RIYAZI MESELE HELLI<<<")
print("Eger programi dayandirmaq isteseniz , operator daxil edin hissesine X yazmaginiz ve ENTER basmaginiz yeterlidir.")
ilk_eded = int(input("Ilk Edeedi Daxil Edin:"))


class kalkulyator():
    def toplamaq(x, y):
        answer = int(x + y)
        return answer

    def cixmaq(x, y):
        answer = int(x - y)
        return answer

    def vurmaq(x, y):
        answer = int(x*y)
        return answer

    def bolmek(x, y):
        answer = int(x/y)
        return answer


while True:
    x = input("Operatoru Daxil Edin(-,+,*,/) ve ya Programi Dayanirin:")
    if x == 'X' or x == 'x':
        print("Programi Dayandirdiniz!")
        break
    if (x != '-' and x != '+') and (x != '*' and x != '/'):
        print("Duzgun Operator Daxil Etmediyiniz Ucun Program Dayandirildi!")
        break
    if x == '-':
        a = int(input(("Cixani Daxil Edin:")))
        print(ilk_eded, '-', a, '=', kalkulyator.cixmaq(ilk_eded, a))
        ilk_eded = kalkulyator.cixmaq(ilk_eded, a)
    if x == '+':
        a = int(input(("Toplanani Daxil Edin:")))
        print(ilk_eded, '+', a, '=', kalkulyator.toplamaq(ilk_eded, a))
        ilk_eded = kalkulyator.toplamaq(ilk_eded, a)
    if x == '*':
        a = int(input(("Vurani Daxil Edin:")))
        print(ilk_eded, '*', a, '=', kalkulyator.vurmaq(ilk_eded, a))
        ilk_eded = kalkulyator.vurmaq(ilk_eded, a)
    if x == '/':
        a = int(input(("Boleni Daxil Edin:")))
        ilk_eded = kalkulyator.bolmek(ilk_eded, a)
        print(ilk_eded, '/', a, '=', kalkulyator.bolmek(ilk_eded, a))
