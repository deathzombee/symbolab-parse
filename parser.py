import json

with open("steps.json") as f:
    data = json.load(f)


# Function to format the solution steps for Obsidian
def format_individual_steps(steps):
    formatted_steps = []
    for step in steps:
        if "title" in step:
            formatted_steps.append(f"$$\n{step['title']}\n$$")
        if "steps" in step:
            formatted_steps.extend(format_individual_steps(step["steps"]))
        else:
            if "primary" in step:
                formatted_steps.append(f"$$\n{step['primary']}\n$$")
            if "result" in step:
                formatted_steps.append(f"$$\n{step['result']}\n$$")
    return formatted_steps


# Extract steps from the JSON and format them
steps = data["solution"]["steps"]["steps"]
formatted_output = format_individual_steps(steps)

formatted_output_str = "\n".join(formatted_output)

# confirm the output
print(formatted_output_str)
print("\n\n\n\n\n")
print(steps)
