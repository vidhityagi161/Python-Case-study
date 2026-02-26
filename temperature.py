

def classify_temperature(temp):
   
    if temp < 18:
        return "Cold"
    elif temp <= 28:
        return "Normal"
    else:
        return "Hot"

def calculate_statistics(temperatures):
   
    if not temperatures:
        return 0, 0, 0
    
    average = sum(temperatures) / len(temperatures)
    highest = max(temperatures)
    lowest = min(temperatures)
    
    return average, highest, lowest

def count_conditions(temperatures):
   
    counts = {"Hot": 0, "Normal": 0, "Cold": 0}
    
    for temp in temperatures:
        condition = classify_temperature(temp)
        counts[condition] += 1
    
    return counts

def determine_actions(counts):
   
    actions = []
    
    if counts["Hot"] > 0:
        actions.append("Fan ON")
    if counts["Cold"] > 0:
        actions.append("Heater ON")
    
    return actions

def display_report(temperatures, average, highest, lowest, counts, actions):
  
    print("\n" + "="*40)
    print("TEMPERATURE SUMMARY REPORT")
    print("="*40)
    
    print(f"\nAverage Temperature: {average:.1f}")
    print(f"Highest Temperature: {highest:.1f}")
    print(f"Lowest Temperature: {lowest:.1f}")
    
    print(f"\nCondition Counts:")
    print(f"  Hot: {counts['Hot']}")
    print(f"  Normal: {counts['Normal']}")
    print(f"  Cold: {counts['Cold']}")
    
    print(f"\nSuggested Action(s):")
    if actions:
        for action in actions:
            print(f"  - {action}")
    else:
        print("  - No action required")
    
    print("\n" + "="*40)

def main():
    """
    Main function to run the temperature monitoring system.
    """
    print("Temperature Monitoring and Control System")
    print("-" * 40)
    
   
    while True:
        try:
            num_readings = int(input("Enter number of readings: "))
            if num_readings > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    
    temperatures = []
    print("\nEnter temperature readings:")
    
    for i in range(num_readings):
        while True:
            try:
                temp = float(input(f"  Reading {i+1}: "))
                temperatures.append(temp)
                break
            except ValueError:
                print("    Invalid input. Please enter a valid temperature.")
    
   
    average, highest, lowest = calculate_statistics(temperatures)
    
    
    counts = count_conditions(temperatures)
    
  
    actions = determine_actions(counts)
    
   
    display_report(temperatures, average, highest, lowest, counts, actions)


if __name__ == "__main__":
    main()