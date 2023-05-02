from argparse import ArgumentParser
import sys

#to be implemented in Party() class
def __str__(self):
    """Returns informal string representation of party information for guests
    """
    return f"Host: {self.host}" \
        f"Address: {self.address}" \
            f"Type: {self.type}" \
                f"Service: {self.service}" \
                    f"Time: {self.time_start} to {self.time_end}"

#to be implemented in Party() class
def __repr__(self):
    """Returns a formal str representation of party information for guests
    """
    return f"You have been invited to a {self.type} party by {self.host}." \
        f"The location will be {self.address}." \
            f"The time will be from {self.time_start} to {self.time_end}." \
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

def main():
    pass

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
    