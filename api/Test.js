// Test.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Test = () => {
  const [quizzes, setQuizzes] = useState([]);
  const [answers, setAnswers] = useState({});
  const [isSubmitted, setIsSubmitted] = useState(false);

  useEffect(() => {
    // Fetch quizzes from the API
    const fetchQuizzes = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/quizzes/');
        setQuizzes(response.data);
      } catch (error) {
        console.error('Error fetching quizzes:', error);
      }
    };

    fetchQuizzes();
  }, []); // Run this effect only once on component mount

  const handleOptionChange = (questionId, selectedOption) => {
    setAnswers({
      ...answers,
      [questionId]: selectedOption,
    });
  };

  const handleSubmit = () => {
    // Perform actions on quiz submission, e.g., display correct answers
    setIsSubmitted(true);
  };

  const handleRetake = () => {
    // Reset state for a retake
    setAnswers({});
    setIsSubmitted(false);
  };

  return (
    <div>
      <h2>Test</h2>
      {quizzes.map((quiz) => (
        <div key={quiz.id}>
          <p>{quiz.question}</p>
          {quiz.options.map((option) => (
            <label key={option}>
              <input
                type="radio"
                value={option}
                checked={answers[quiz.id] === option}
                onChange={() => handleOptionChange(quiz.id, option)}
                disabled={isSubmitted}
              />
              {option}
            </label>
          ))}
          <br />
        </div>
      ))}
      <button onClick={handleSubmit} disabled={isSubmitted}>
        Submit
      </button>
      <button onClick={handleRetake} disabled={!isSubmitted}>
        Retake Quiz
      </button>
      {isSubmitted && (
        <div>
          <h3>Results:</h3>
          {quizzes.map((quiz) => (
            <div key={quiz.id}>
              <p>{quiz.question}</p>
              <p>Correct Answer: {quiz.correctOption}</p>
              <p>Your Answer: {answers[quiz.id]}</p>
              <p>Is Correct: {answers[quiz.id] === quiz.correctOption ? 'Yes' : 'No'}</p>
              <br />
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Test;
