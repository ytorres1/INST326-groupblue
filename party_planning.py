import math
import re
from argparse import ArgumentParser
import sys
import pandas as pd
import matplotlib.pyplot as plt

class Guests():
    
    def __init__(self, file):
        """Initializes the guest list with the guests from the file
        
        Attributes:
            guests (list of dictionaries): names of guests
        """
        self.guests = []
        with(open(file, "r", encoding = "utf-8")) as f:
            for line in f:
                if (line.find(':') == -1):
                    regex = (r"""(?x)^
                             (?P<name>\w+?\s\w+?)\s
                             (?P<rsvp>\w+?)\s
                             (?P<dietres>.+?)\s
                             (?P<phone>\d+?)\s
                             (?P<gender>\w)\s
                             (?P<age>\d+?)$""")
                    match = re.search(regex, line)
                    thisGuest = {"Name":match.group("name"), 
                                 "RSVP":match.group("rsvp"),
                                 "Diet Res":match.group("dietres"), 
                                 "Phone":match.group("phone"),
                                 "Gender":match.group("gender"), 
                                 "Age":match.group("age")}
                    self.guests.append(thisGuest)
                    
    def confirmed_guests(self):
        """Creates a list of guests who have their RSVP status as 'Yes.'
        
        Returns:
            list (list of strings): list of guests who have RSVP to the party. 
        """
        confirmed_guests = []   
        unconfirmed_guests = []           
        for item in self.guests:
            (confirmed_guests.append(item.get("Name")) if item.get("RSVP") == 
             "Yes" else unconfirmed_guests.append(item.get("Name")))
    
        return confirmed_guests
        
    def seating_chart(self):
        """Creates a list of an appropriate amount of tables that are 
            full of guests. 
            
        Returns:
            list (lists of strings): list of the guests grouped in tables
                for the approrpriate amount of guests at a party.
                
        Primary Author:
            Yasmine Torres
            
        Technique Demonstrated: 
            List Comprehension
        """
        
        temp_guest_list = Guests.confirmed_guests(self)
        total_guests = len(self.guests)
        
        total_tables = math.ceil(total_guests / 10)
        people_per_table = math.ceil(total_guests / total_tables)
        
        chart = ([temp_guest_list[index: index + people_per_table] 
                    for index in range(0, len(temp_guest_list), 
                        people_per_table)])
        
        return chart
    
    def sorted_guests(self, chart):
        """Sorts the list of guests in alphabetical order by last name. 
        
        Args:
            chart (list of lists): a list with the guests grouped by table 
                generated from the seating_chart method
                
        Returns:
            dict: dictionary of guests with guest name as key and their 
                table number as value. 
                
        Primary Author:
            Yasmine Torres
            
        Technique Demonstrated: 
            Sort using Lambda
        """
        
        new_dict = {}
        for table in chart:
            for name in table:
                new_dict[name] = f'Table Number: {chart.index(table) + 1}'
        sorted_dict = sorted(new_dict.items(), key=lambda x: x[0].split()[1])
        return sorted_dict
    
    def guest_details(self, name):
        """Returns the information details of a single guest when asked.
        
        Args:
            name (str): the name of the person that you want the information of.
            
        Returns: 
            dict: new dictionary that includes details of the specified guest, 
                if the guest can not be found will return None.
                
        """
        
        new_dict = {}
        for guest in self.guests:
            if guest["Name"] == name:
                return guest
        #return the name of the guest if input matches the name in the text file
        return None
    
    def guest_stats(self):
        """Reads a guest list in the form of CSV file using pandas to perform 
            various analyses with the data.

        Args:
        None

        Returns:
        None
        """
        df_name = input("Please provide the name of the csv you want to use. " 
                        "Make sure to add the .csv\n")
        df = pd.read_csv(df_name)

        # Guest List with RSVP status and pertinent dietary restrictions
        guestlist_df = df.loc[:, ['First Name', 'Last Name', 'RSVP Status']]
        print(guestlist_df)
        print(df['Dietary Restriction'].unique())


        #gender count bar graph
        sex_df = df['Sex'].value_counts()
        print(sex_df)
        sex_df.plot.bar(x=['Male', 'Female'], y=sex_df)

        #age group bar graph
        #create groups by age
        children = df['Age'] <= 12
        teenagers = (df['Age'] > 12) & (df['Age'] <= 21)
        adults = df['Age'] > 21

        #Creates df with data from above and plots the graph
        age_groups = ['Children', 'Teenagers', 'Adults']
        age_counts = [len(df[children]), len(df[teenagers]), len(df[adults])]
        age_counts_df = pd.DataFrame({'Age Group': age_groups, 
                                      'Count': age_counts})
        age_counts_df.plot.bar(x='Age Group', y='Count')

        plt.show() # Add this line to display the graphs

class Party():
    """class for Party object
    
    Attributes:
        host (str): the host of the party
        address (str): the address of the party
        budget (int): budget for the party
        type (str): type of party
        service (str): type of food service
        time_start (str): start of party
        time_end (str): end of party
        guests (str): a Guest object 
    """
    
    def __init__(self, file):
        with open(file, "r", encoding = "utf-8") as f:
            for line in f:
                if(line.find(':') == -1):
                    continue
                if "Hostname" in line:
                    self.host = line[line.find(':')+2:]
                    continue
                if "Location" in line:
                    self.address = line[line.find(':')+2:]
                    continue
                if "Time" in line:
                    self.time_start = line[line.find(':')+2:line.find('-')]
                    self.time_end = line[line.find('-'):]
                    continue
                if "Budget" in line:
                    self.budget = int(line[line.find('$')+1:])
                    continue
                if "PartyType" in line:
                    self.type = line[line.find(':')+2:]
                    continue
                if "FoodService" in line:
                    self.service = line[line.find(':')+2:]
                    continue
        
        self.guests = Guests(file)
    
    def __str__(self):
        """Returns informal string representation of party information for 
            guests.
        """
        return f"Host: {self.host}" \
            f"Address: {self.address}" \
            f"Type: {self.type}" \
            f"Service: {self.service}" \
            f"Time: {self.time_start}{self.time_end}"

    def __repr__(self):
        """Returns a formal str representation of party information for guests.
        """
        return f"You have been invited to a {self.type} party by {self.host}." \
            f"The location will be {self.address}." \
            f"The time will be from {self.time_start}{self.time_end}." \
            f"This party will provide {self.service} service."

def parse_args(arglist):
    """Parse command-line arguments.
    
    Expects one mandatory command-line argument: a path to a text file with 
        the party information
    
    Args:
        arglist (list of str): a list of command-line arguments to parse.
        
    Returns:
        argparse.Namespace: a namespace object with a file attribute whose value
        is a path to a text file as described above.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="file of party information")
    return parser.parse_args(arglist)

    
def main(path):
    current = Guests(path)
    while True:
        choice = input('''What do you want to see? 
                    #1 Guests who have RSVP 
                    #2 Seating chart for guests
                    #3 List of seating chart for waiter
                    #4 Visualize all your guests details
                    #5 Find one specific guest's details
                    #6 View all party details 
                    #7 Invitation to your guests
                    Type "done" if you are finished
                    Your choice: ''')
        if choice == "1": 
            print(current.confirmed_guests())
        elif choice == "2":
            print(current.seating_chart())
        elif choice == "3":
            print(current.sorted_guests(current.seating_chart()))
        elif choice == "4":
            print(current.guest_stats())
        elif choice == "5":
            choice2 = input("Enter a guest name here: ")
            print(current.guest_details(choice2))
        elif choice == "6":
            print(Party(path))
        elif choice == '7':
            print(repr(Party(path)))
        elif choice == "done":
            break
        else:
            print("Invalid Choice. Try Again!")
    
        
        
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
        
    
    
    
    
