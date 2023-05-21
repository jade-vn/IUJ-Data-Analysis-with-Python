#First version
daily_returns = [.0015, .0112, -.0012, .0239, .0039, -.0059, -.0081, .0132, .0021]

for return_value in daily_returns:
    if return_value > 0:
        print(f"{return_value} is positive.")
    elif return_value < 0:
        print(f"{return_value} is negative.")
    else:
        print(f"{return_value} is neither positive nor negative.")

#Second version
daily_returns = [.0015, .0112, -.0012, .0239, .0039, -.0059, -.0081, .0132, .0021]

positive_returns = [return_value for return_value in daily_returns if return_value > 0]
negative_returns = [return_value for return_value in daily_returns if return_value < 0]

print(f"Positive returns: {positive_returns}")
print(f"Negative returns: {negative_returns}")

