#!/usr/bin/env python
import os
from dotenv import load_dotenv
from mem0 import memory
from car_dealer.crew import VehicleSalesCrew

load_dotenv()

def run():
    print("Welcome to the Conversational AI Chatbot!")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")
    crew = VehicleSalesCrew().crew()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Assistant: Goodbye! It was nice talking to you.")
            break

        # Add user input to memory
        memory.add(f"User: {user_input}", user_id="user")

        # Retrieve relevant information from vector store
        relevant_info = memory.search(query=user_input, limit=3, user_id="user")

        inputs = {
            "user_message": user_input,
            "relevant_info": relevant_info
        }

        response = crew.kickoff(inputs=inputs)

        # Add chatbot response to memory
        memory.add(f"Assistant: {response}", user_id="assistant")
        print(f"Assistant: {response}")

if __name__ == "__main__":
    run()
