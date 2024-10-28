service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "closed"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
    "Ticket003": {"Customer": "Charlie", "Issue": "Lost item", "Status": "open"}
}
ticket_number = 3
system = True

while system is True:
    new_ticket = int(input("\n Please select an action: \n   1: Open a new ticket \n   2: Update the status of existing ticket \n   3: Display all the tickets \n   4: Exit \n"))
    if new_ticket == 1:
        name = input("What is your first name? ")
        issue = input("What is the issue? ")
        ticket_number += 1
        service_tickets[f"Ticket00{ticket_number}"] = {"Customer": name, "Issue": issue, "Status": "open"}
        print(f"Thank you for your submission. Your ticket number is Ticket00{ticket_number}.")
    elif new_ticket == 2:
        tick_num = input("What is your ticket number? Please enter full, e.g. Ticket001 : ")
        try:
            if service_tickets[tick_num]["Status"] == "closed":
                print(f"The ticket {tick_num} is already closed.")
                additional_action = input("Do you want to reopen it? (yes/no) ")
                if additional_action.lower() == "yes":
                    service_tickets[tick_num]["Status"] = "open"
                    print(f"The ticket {tick_num} has been re-opened.")
                else:
                    print("Thank you for using the ticketing system.")
            elif service_tickets[tick_num]["Status"] == "open":
                print(f"The ticket {tick_num} is open.")
                additional_action = input("Do you want to close it? (yes/no) ")
                if additional_action.lower() == "yes":
                    service_tickets[tick_num]["Status"] = "closed"
                    print(f"The ticket {tick_num} has been closed.")
                else:
                    print("Thank you for using the ticketing system.")
            else:
                print("Invalid entry.")
        except KeyError:
            print(f"This ticket {tick_num} doesn't match. Please double check and try again.")
    elif new_ticket == 3:
        view = input("Choose an option: \n  a. Display all tickets \n  b. Display open tickets \n  c. Dislay closed tickets\n")
        if view == "a":
            for item, info in service_tickets.items():
                print(f"{item}")
                for key, value in info.items():
                    print(f"    {key}: {value}")
        elif view == "b":
            for item, info in service_tickets.items():
                if info["Status"] == "open":
                    print(f"{item}")
                    for key, value in info.items():
                        print(f"    {key}: {value}")
        elif view == "c":
            for item, info in service_tickets.items():
                if info["Status"] == "closed":
                    print(f"{item}")
                    for key, value in info.items():
                        print(f"    {key}: {value}")
        else:
            print("Invalid Entry.")
    elif new_ticket == 4:
        system = False
    else:
        print("Invalid entry. Please try again\n")
