import argparse


# Fixture without yield
def list_fiddling(l):
    l2 = l
    l3 = list(l)
    l2.pop()

    print('l=' + str(l))
    print('l2=' + str(l2))
    print('l3=' + str(l3))

    sl3 = sorted(l3)
    print('sl3=' + str(sl3))

    m = l3.sort()
    print('after sort() l3=' + str(l3))
    print('m=' + str(m))

    print('type of l3:' + str(type(l3)))


def last_person_time(time_data, desk_number):
    # list of customer time slots for each desk
    desk_flow_data = list([])
    cash_range = range(desk_number)
    for cash in cash_range:
        desk_flow_data.append([])
    num_desk_flows = len(desk_flow_data)
    #for slot in time_data:
    for customer_number in range(len(time_data)):
        num = get_next_avalable_desk_number(desk_flow_data)
        desk_flow_data[num].append(time_data[customer_number])
        print(f"sending customer's {customer_number} slot {time_data[customer_number]} to {num} desk")

        if customer_number == len(time_data) - 1:
            print(f"last customer {customer_number} assigned to {num} desk")
            # calculating full time for the last customer's desk
            last_customer_time = sum(desk_flow_data[num])
            print(f"service time for the last customer is {last_customer_time}")

    sum_vals = [sum(cash_flow) for cash_flow in desk_flow_data]
    ft = max(sum_vals)
    print(f"full service time is {ft}")
    return last_customer_time


def get_next_avalable_desk_number(flow_data):
    sum_vals = [sum(cash_flow) for cash_flow in flow_data]
    print('current cash_flows ' + str(sum_vals))
    ind = sum_vals.index(min(sum_vals))
    print('chosing ' + str(ind) + ' desk')
    return ind


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="mock_server_url",
                        help="Mock Server URL",
                        default="http://stats-qa-03:8888")
    parser.add_argument("-o", "--order_id", dest="order_id",
                        help="Order Id",
                        default="81b0314a-9e90-4657-bed6-b00aa3468007")

    args = parser.parse_args()

    mylist = [3, 6, 1, 1, 87, 12, 5]
    myemptylist =[]

    listsum = sum(mylist)
    mv = min(mylist)
    idx = mylist.index(mv)
    print('listsum=' + str(listsum))

    emptysum = sum(myemptylist)
    print('emptysum=' + str(emptysum))

    print('mv=' + str(mv))
    print('idx=' + str(idx))
    result = last_person_time(mylist, 3)


