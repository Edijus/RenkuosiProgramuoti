import tkinter as tk
from budget import Budget
import enum


class State(enum.Enum):
    stDefault = 0
    stAskRevenueAmount = 1
    stAskExpenseAmount = 2
    stAskSender = 3


budget = Budget()

main_input_text = '1 - Add revenue record \n2 - Add expense record \n3 - Show balance \n4 - Show report \n5 - Exit '

window = tk.Tk()
window.title('Budget')
window.geometry("300x300")
label = tk.Label(window, text=main_input_text, wraplength=250, justify="left")
entry_amount_label = tk.Label(window, text='Enter amount:', wraplength=250, justify="left")
action_entry = tk.Entry(window)  # input field

state = State.stDefault
action = 0
amount = 0


def ask_input(text: str):
    label.config(text=text)
    action_entry.delete(0, 'end')


def set_state(st: State, text: str):
    global state
    state = st
    ask_input(text)


def handle_action_button():
    global state
    global action
    action = 0
    if state == State.stDefault:
        action = int(action_entry.get())
        action_entry.delete(0, 'end')
        print('default', action)
        if action == 1:
            print(action)
            set_state(State.stAskRevenueAmount, 'Enter revenue amount:')
        elif action == 2:
            print(action)
            set_state(State.stAskExpenseAmount, 'Enter expense amount:')
        elif action == 3:
            budget.show_balance()
            set_state(State.stDefault, main_input_text)
        elif action == 4:
            budget.show_report()
            set_state(State.stDefault, main_input_text)
        elif action == 5:
            print('Bye')
            window.destroy()
        else:
            print('Unknown action')

        return

    elif state == State.stAskRevenueAmount:
        print(state)
        global amount
        amount = float(action_entry.get())
        set_state(State.stAskSender, 'Enter sender:')
    elif state == State.stAskSender:
        budget.add_revenue_record(amount, action_entry.get())
        set_state(State.stDefault, main_input_text)
    elif state == State.stAskExpenseAmount:
        print(state)
        amount = float(action_entry.get())
        budget.add_expense_record(amount)
        set_state(State.stDefault, main_input_text)


button = tk.Button(window, text='Hit me', command=handle_action_button)
label.pack()
action_entry.pack(padx=1, pady=1)
button.pack(padx=1, pady=10)
window.mainloop()
