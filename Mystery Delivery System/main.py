import json
import math
import csv



# Function to calculate distance between points

def calculate_distance(point1, point2):

    # Using Euclidean distance formula
    distance = math.sqrt(
        (point2[0] - point1[0]) ** 2 +
        (point2[1] - point1[1]) ** 2
    )

    return distance



# Function to load JSON data file

def load_data(file_path):

    # Open the JSON file
    with open(file_path, "r") as file:
        data = json.load(file)

    return data



# Function to assign packages to nearest agent

def assign_packages(data):

    warehouses = data["warehouses"]
    agents = data["agents"]
    packages = data["packages"]

    assignments = {}

    # Go through every package
    for package in packages:

        warehouse_id = package["warehouse"]
        warehouse_location = warehouses[warehouse_id]

        nearest_agent = None
        minimum_distance = float("inf")

        # Check distance from every agent
        for agent_id, agent_location in agents.items():

            distance = calculate_distance(
                agent_location,
                warehouse_location
            )

            # If this agent is closer, update nearest agent
            if distance < minimum_distance:
                minimum_distance = distance
                nearest_agent = agent_id

        # Add package to that agent
        if nearest_agent not in assignments:
            assignments[nearest_agent] = []

        assignments[nearest_agent].append(package)

    return assignments



# Function to simulate deliveries

def simulate_deliveries(data, assignments):

    warehouses = data["warehouses"]
    agents = data["agents"]

    report = {}

    # Go through every agent
    for agent_id, package_list in assignments.items():

        current_location = agents[agent_id]

        total_distance = 0
        delivered_packages = 0

        print(f"\nDelivery Route For {agent_id}")

        # Deliver all assigned packages
        for package in package_list:

            warehouse_location = warehouses[package["warehouse"]]
            destination = package["destination"]

            # Distance from current location to warehouse
            distance_to_warehouse = calculate_distance(
                current_location,
                warehouse_location
            )

            # Distance from warehouse to customer
            distance_to_destination = calculate_distance(
                warehouse_location,
                destination
            )


            # Total trip distance
            trip_distance = (
                distance_to_warehouse +
                distance_to_destination
            )

            total_distance += trip_distance
            delivered_packages += 1

            # Agent moves to new destination
            current_location = destination

            # Print route details
            print(
                f"{agent_id} -> {package['warehouse']} -> {package['id']}"
            )

            print(
                f"Delivered at {destination} | "
                f"Distance Travelled: {trip_distance:.2f}"
            )

        # Average distance per package
        efficiency = total_distance / delivered_packages

        # Save agent report
        report[agent_id] = {
            "packages_delivered": delivered_packages,
            "total_distance": round(total_distance, 2),
            "efficiency": round(efficiency, 2)
        }

    return report


# Function to find best performing agent

def find_best_agent(report):

    # Lower efficiency score means better performance
    best_agent = min(
        report,
        key=lambda agent: report[agent]["efficiency"]
    )

    return best_agent



# Function to save report in JSON file

def save_report(report, file_name="report.json"):

    with open(file_name, "w") as file:
        json.dump(report, file, indent=4)



# Function to export best agent into CSV

def export_top_performer(report, best_agent):

    with open("top_performer.csv", "w", newline="") as file:

        writer = csv.writer(file)

        # CSV headings
        writer.writerow([
            "Agent",
            "Packages Delivered",
            "Total Distance",
            "Efficiency"
        ])

        # Best agent data
        writer.writerow([
            best_agent,
            report[best_agent]["packages_delivered"],
            report[best_agent]["total_distance"],
            report[best_agent]["efficiency"]
        ])



# Main function

def main():

    # Step 1 - Load data from JSON file
    data = load_data("data.json")

    # Step 2 - Assign packages
    assignments = assign_packages(data)

    print("\nPACKAGE ASSIGNMENTS")

    # Print assigned packages
    for agent, packages in assignments.items():

        package_ids = []

        for package in packages:
            package_ids.append(package["id"])

        print(f"{agent}: {package_ids}")

    # Step 3 - Start delivery simulation
    report = simulate_deliveries(data, assignments)

    # Step 4 - Find best agent
    best_agent = find_best_agent(report)

    # Add best agent to report
    report["best_agent"] = best_agent

    # Step 5 - Save JSON report
    save_report(report)

    # Step 6 - Export best performer CSV
    export_top_performer(report, best_agent)

    # Final report output
    print("\nFINAL REPORT")

    print(json.dumps(report, indent=4))



# Program starts from here

if __name__ == "__main__":
    main()