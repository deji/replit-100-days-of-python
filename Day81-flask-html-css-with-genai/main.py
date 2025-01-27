from flask import Flask, request

app = Flask(__name__)

css_style = """

<style>
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }

    body {
        background-color: #f0f2f5;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
        padding: 20px;
    }

    .form-container {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        width: 100%;
        max-width: 500px;
    }

    h2 {
        color: #333;
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .form-group {
        margin-bottom: 1.5rem;
    }

    label {
        display: block;
        margin-bottom: 0.5rem;
        color: #555;
        font-weight: 500;
    }

    input[type="text"],
    input[type="email"],
    select {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }

    input[type="text"]:focus,
    input[type="email"]:focus,
    select:focus {
        outline: none;
        border-color: #4a90e2;
    }

    .radio-group {
        display: flex;
        gap: 1rem;
        margin-top: 0.5rem;
    }

    .radio-option {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .required-label::after {
        content: " *";
        color: #ff4444;
    }

    button {
        background-color: #4a90e2;
        color: white;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 5px;
        font-size: 1rem;
        cursor: pointer;
        width: 100%;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #357abd;
    }

    @media (max-width: 480px) {
        .form-container {
            padding: 1rem;
        }

        .radio-group {
            flex-direction: column;
            gap: 0.5rem;
        }
    }
</style>

"""


@app.route('/')
def index():
    return f"""

<!DOCTYPE html>
<html>
<head>
    {css_style}
</head>
<body>
    <div class="form-container">
        <h2>Contact Form</h2>
        <form method="POST" action="/process">

            <div class="form-group">
                <label class="required-label">Are you made of metal?</label>
                <div class="radio-group">
                    <div class="radio-option">
                        <input type="radio" id="yes-preference" name="madeofmetal" value="yes" required>
                        <label for="yes-preference">Yes</label>
                    </div>
                    <div class="radio-option">
                        <input type="radio" id="no-preference" name="madeofmetal" value="no" required>
                        <label for="no-preference">No</label>
                    </div>
                </div>
            </div>
            
            <div class="form-group">
                <label for="question" class="required-label">What is infinity + 1?</label>
                <input type="text" id="question" name="question" required placeholder="Solve this and prove your humanity!">
            </div>

            <div class="form-group">
                <label for="favouritefood" class="required-label">Which is your favourite food?</label>
                <select id="favouritefood" name="favouritefood" required>
                    <option value="">Select a food</option>
                    <option value="grease_oil">Grease & Oil</option>
                    <option value="macaroni_cheese">Macaroni & Cheese</option>
                    <option value="vegetables">Vegetables</option>
                </select>
            </div>

            <button type="submit">Submit Form</button>
        </form>
    </div>
</body>
</html>

"""


@app.route('/process', methods=['POST'])
def process():
    # {"favouritefood":"vegetables","madeofmetal":"no","question":"How do you suppose I know this?!?!?!"}
    data = request.form
    machine_score = 0
    if data['madeofmetal'] == 'yes':
        machine_score += 1
    if data['favouritefood'] == 'grease_oil':
        machine_score += 1
    if data['question'].lower().strip() == 'infinity':
        machine_score += 1

    if machine_score == 3:
        result = "You are a machine!"
    elif machine_score == 2:
        result = "You are probably a machine!"
    else:
        result = "You are human!"

    return f"""

<!DOCTYPE html>
<html>
<head>
    {css_style}
</head>
<body>
    <div class="form-container">
        <h2>Result!</h2>
        {result}
    </div>
</body>
    
"""


app.run(host='0.0.0.0', port=81)
