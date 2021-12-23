'''
Author: Katam Vamsi Krishna
github handle: kvamsi7
'''

# months as dictionary form
months = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
rev_lookup_months = {v:k for k,v in months.items()}


def sort_the_months(inp_arr):
    """
    sort the months in chronological order and return them

    Args:
        inp_arr (string): raw input which contain the month index positions

    Returns:
        list: a list of month names in sorted order(chronologically)
    """
 
    if inp_arr != '':

        inp_list = []
        for i in inp_arr.split(): 
            inp_list.append(int(i.strip()))
        in_months = [rev_lookup_months.get(i,0) for i in inp_list] # picking up the month names using reverse lookup
        return sorted(in_months,key=months.get)                    # sorting the months on basis of index
    else:
        return []

if __name__ == '__main__':
    inp_arr = input("please enter the months in numerical form(1 to 12).. \n Ex: 1 for 'January'\n     2 for 'February'\n")
    sorted_list = sort_the_months(inp_arr)

    print(sorted_list)
