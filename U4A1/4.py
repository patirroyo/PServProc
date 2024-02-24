#Enter an IP or host address and have it look it up through whois and return the results to you. 

import whois

def whois_lookup(target):
    try:
        # Perform WHOIS lookup
        result = whois.whois(target)
        return result
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    target = input("Enter an IP address or host name: ")
    result = whois_lookup(target)

    if isinstance(result, dict):
        print("\nWHOIS Lookup Results:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(result)

if __name__ == "__main__":
    main()
