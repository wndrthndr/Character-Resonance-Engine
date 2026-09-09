// hooks/useQuiz.ts
export async function fetchQuestions(franchise: string) {
    const response = await fetch(`http://127.0.0.1:8000/api/questions?franchise=${franchise}&limit=5`);
    if (!response.ok) throw new Error("Failed to fetch questions");
    return response.json();
  }