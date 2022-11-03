melon_cost = 1.00

def customer_payments(customer_data):
    customer_information = open(customer_data)

    for line in customer_information:

        info = line.split("|")
        customer_name = info[1]
        given_name = customer_name.split(" ")[0]
        quantity_melons = float(info[2])
        price_paid = float(info[3])
        expected = quantity_melons * melon_cost

        print(f"{customer_name} paid ${price_paid}, expected to pay ${expected}.")

    customer_information.close()

customer_payments("customer-orders.txt")
