### Week 2 – Conversational LLMs & Prompt Engineering

## Part 1: Understanding Chat Roles

- **system** → sets the rules, personality, and behavior of the AI  
- **user** → represents the human input  
- **assistant** → the AI’s generated response 

Example (JSON format):

[
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Hello"},
  {"role": "assistant", "content": "Hi! How can I help you today?"}
]

### Part 2: Persona Experimentation

## Prompt:
User: “Explain black holes in 2 sentences.”

Persona 1 – Professional Assistant

System Prompt: You are a professional assistant. Be concise and formal.

Output:
A black hole is a region of space where gravity is so strong that not even light can escape. They form when massive stars collapse under their own gravity.

Persona 2 – Creative Companion

System Prompt: You are a creative companion. Use humor and imagination.

Output:
Imagine a cosmic vacuum cleaner so powerful it even slurps up light—that’s a black hole. It’s the universe’s way of saying, “what goes in here, stays here.”

Persona 3 – Fitness Coach

System Prompt: You are a fitness coach. Be motivational and practical.

Output:
A black hole is like the ultimate “no-escape zone,” where gravity wins every rep. Just like in training, once you’re in its grip, there’s no skipping the workout!

### Part 3: CLI Chatbot (Simulated Example)

## Example Run (Persona = Creative Companion):

Choose a persona:
1. Professional Assistant
2. Creative Companion
3. Fitness Coach
Enter 1/2/3: 2

Type 'exit' to quit.

You: What is AI?
AI: Think of AI as a clever apprentice that learns patterns from mountains of data. 
    It doesn’t dream of electric sheep yet, but it sure can write you a poem about them!

You: exit
Chat ended.

### My reflections
So, in short if i explain that when i need to talk to chatgpt or any ai modal i should first set the system prompt. Suppose i am a react developer and i want some hooks knowledge from it So i would say you are a react developer and explain me useEffect hook.
[
  {
    "role": "system",
    "content": "You are a senior React developer. Explain React hooks with clear, beginner-friendly examples."
  },
  {
    "role": "user",
    "content": "Can you explain the useEffect hook with an example?"
  },
  {
    "role": "assistant",
    "content": "Sure! The `useEffect` hook lets you run side effects in a function component. Think of it like saying: *after React renders this component, also do this extra work.*\n\nExample:\n\n```jsx\nimport React, { useState, useEffect } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n\n  // useEffect runs after render\n  useEffect(() => {\n    document.title = `You clicked ${count} times`;\n  }, [count]); // runs only when 'count' changes\n\n  return (\n    <div>\n      <p>You clicked {count} times</p>\n      <button onClick={() => setCount(count + 1)}>Click me</button>\n    </div>\n  );\n}\n```\n\nHere, `useEffect` updates the page title every time `count` changes. Without it, React would render the UI but not touch the document title."
  }
]
