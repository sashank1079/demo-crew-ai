#!/usr/bin/env python
import os
from dotenv import load_dotenv
from car_dealer.crew import VehicleSalesCrew
from mem0 import Memory


load_dotenv()

config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "chatbot_memory",
            "path": "./chroma_db",
        },
    },
}

memory = Memory.from_config(config)

def run():
    print("Welcome to Car Dealership!")
    print("Type 'exit', 'quit', or 'bye' to end the conversation.")

    # Initialize the crew
    vehicle_sales_crew = VehicleSalesCrew()
    crew = vehicle_sales_crew.crew()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! It was nice talking to you.")
            break

        # Add user input to memory
        memory.add(f"User: {user_input}", user_id="user")

        # Retrieve relevant information from vector store
        relevant_info = memory.search(query=user_input, limit=3, user_id="user")

        # Decide the appropriate task based on user input
        task_name = vehicle_sales_crew.decide_task(user_input)

        inputs = {
            "user_message": user_input,
            "context": relevant_info  # Provide enriched context to the crew
        }

        # Generate response using the crew's kickoff method
        response = crew.kickoff(inputs=inputs)

        # Add chatbot response to memory
        memory.add(f"Assistant: {response}", user_id="assistant")
        print(f"Assistant: {response}")


if __name__ == "__main__":
    run()
