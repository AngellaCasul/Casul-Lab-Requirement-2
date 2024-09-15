from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate the required grades using the updated formula
def calculate_required_grades(prelim_grade):
    prelim_weight = 0.20
    midterm_weight = 0.30
    finals_weight = 0.50
    passing_grade = 75

    # Calculate the prelim contribution (a = prelim_grade * prelim_weight)
    a = prelim_grade * prelim_weight

    # Calculate the combined weight of midterms and finals (b = midterm_weight + finals_weight)
    b = midterm_weight + finals_weight

    # Calculate the remaining contribution required to pass (y = passing_grade - a)
    y = passing_grade - a

    # Calculate the required midterm and final grade average (x = y / b)
    required_midterm_final = y / b

    # Check for various conditions based on the required grades
    if required_midterm_final > 100:
        return f"Unfortunately, you cannot pass with your Prelim grade. You need an average of {required_midterm_final:.2f}, which is impossible."
    elif required_midterm_final < 0:
        return "Congratulations! You've already secured a passing grade."
    else:
        return f"You need an average of at least {required_midterm_final:.2f} in both Midterms and Finals to pass."

# Home route that displays the form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Get the prelim grade from the form
            prelim_grade = float(request.form['prelim_grade'])
            
            # Ensure the input grade is valid
            if prelim_grade < 0 or prelim_grade > 100:
                result = "Invalid input. Prelim grade should be between 0 and 100."
            else:
                # Call the function to calculate the required midterm and final grades
                result = calculate_required_grades(prelim_grade)
        except ValueError:
            result = "Invalid input. Please enter a numerical value for the Prelim grade."

        # Render the result
        return render_template('result.html', result=result)
    
    # On GET request, show the form
    return render_template('index.html')

# Running the app
if __name__ == '__main__':
    app.run(debug=True)
