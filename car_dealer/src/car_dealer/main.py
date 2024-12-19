#!/usr/bin/env python
import os
from dotenv import load_dotenv
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


        inputs = {
            "user_message": user_input,
        }

        response = crew.kickoff(inputs=inputs)

        print(f"Assistant: {response}")

if __name__ == "__main__":
    run()
