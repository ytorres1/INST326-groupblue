INST326-groupblue

Repository for our final project
  -

**Files and purpose**
- `guest1.csv`: file containing guest information for first sample party
- `guest2.csv`: file containing guest information for second sample party 
- `party_file1.txt`: first sample file containing party and guest information 
- `party_file2.txt`: second sample file containing party and guest information
- `party_planning.py`: file containing the program and all code used to perform the necessary techniques for party planning for the user. 

**How to run our program from the command line**
- In the terminal, type in `python3` (on macOS) or `python` (on Windows) followed by a space and the name of the program which is `party_planning.py`. The program takes in a text file as the comamand-line argument. There are two text files provided `party_file1.txt` and `party_file2.txt`

`python3 party_planning.py party_file1.txt`

**How to use our program and/or interpret the output of the program**
- Select an option from the menu provided
  -For #1 Guests who have RSVPed
    -The list returned will contain all guests who have RSVPed 'Yes'
  -For #2 Seating Chart for Guests
    -List returned, each list within that list is a seperate table
  -For #3 List of Seating Chart for Waiter
    -Dictionary returned, sorted in alphabetical order, with guest name as key and 
    table number as value
  -For #4 Visualize all your Guests' details
    -Shows graphs to visualize demographics of Guests
  -For #5 Find one specific guest's details
    -Returns a list of dictionaries, a specific guest's details
  -For #6 View all party details
    -Prints party details
  -For #7 Invitation to your guests
    -Prints party invitation

**Annotated bibliography** 
- all sources used to develop our project. For each source, explain how we used the source.
“Pandas.DataFrame.Loc#.” Pandas.DataFrame.Loc - Pandas 2.0.1 Documentation, pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html. Accessed 11 May 2023. 
- This source was used to better understand how to use .loc to properly split up dataframes using pandas.

**Attribution Table**
| Method/function | Primary Author | Techniques Demonstrated |
| --- | --- | --- |
| `seating_chart()` | Yasmine Torres | List Comprehension |
| `sorted_guests()` | Yasmine Torres | Sort using Lambda |
| Guests '__init__' | Alice Sun      | Regular Expressions|
| Party '__init__'  | Alice Sun      | With Statement |
| Row 5, Column 1 | Row 5, Column 2 | Row 5, Column 3 |
| Row 6, Column 1 | Row 6, Column 2 | Row 6, Column 3 |
| Row 7, Column 1 | Row 7, Column 2 | Row 7, Column 3 |
| Row 8, Column 1 | Row 8, Column 2 | Row 8, Column 3 |
