from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.metrics.pairwise import euclidean_distances

app = Flask(__name__)

# Dataset
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Math': [95, 55, 88, 45],
    'Writing': [60, 92, 65, 95],
    'Coding': [90, 40, 85, 35],
    'Social': [50, 85, 55, 90]
}
df = pd.DataFrame(data).set_index('Student')

@app.route('/')
def home():
    # 'student_list' is the key we are sending to the HTML
    return render_template('index.html', student_list=df.index.tolist())
@app.route('/match', methods=['POST'])
def match():
    selected_student = request.form.get('student')
    
    if not selected_student or selected_student not in df.index:
        return jsonify({"error": "Invalid student selected"}), 400

    # AI Logic: Find the most different (complementary) student
    dist_matrix = euclidean_distances(df)
    dist_df = pd.DataFrame(dist_matrix, index=df.index, columns=df.index)
    
    scores = dist_df[selected_student]
    best_match = scores[scores > 0].idxmax()
    
    # Calculate Synergy Percentage
    synergy_score = round(min((scores[best_match] / 80) * 100, 100), 1)

    return jsonify({
        'user': selected_student,
        'partner': best_match,
        'synergy': synergy_score
    })

if __name__ == '__main__':
    app.run(debug=True)