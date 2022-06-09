'''
3 užduotis
Patobulinti 5 pamokos biudžeto programą:
Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų visas savybes.
Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų įrašyti.
Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir gauti_ataskaita kad pasiėmus įrašą iš žurnalo, atpažintų, ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.
'''

from budget import Budget

budget = Budget()

while True:
    action = int(input('1 - Add revenue record 2 - Add expense record 3 - Show balance 4 - Show report 5 - Exit '))
    if action == 1:
        amount = float(input('Enter amount: '))
        sender = input('Sender: ')
        additional_information = input('Additional information: ')
        budget.add_revenue_record(amount, sender, additional_information)
    elif action == 2:
        amount = float(input('Enter amount: '))
        payment_type = input('Payment type: ')
        product = input('Product: ')
        budget.add_expense_record(amount, payment_type, product)
    elif action == 3:
        budget.show_balance()
    elif action == 4:
        budget.show_report()
    elif action == 5:
        print('Bye')
        break
