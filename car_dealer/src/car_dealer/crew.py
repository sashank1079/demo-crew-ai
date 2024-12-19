from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class VehicleSalesCrew:
    """Crew to assist with vehicle sales interactions"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'



    @agent
    def researcher_agent(self) -> Agent:
        return Agent(
            **self.agents_config['researcher_agent'],
            verbose=False
            
        )

    @agent
    def analyst_agent(self) -> Agent:
        return Agent(
            **self.agents_config['analyst_agent'],
            verbose=False
        )

    @agent
    def sales_agent(self) -> Agent:
        return Agent(
            **self.agents_config['sales_agent'],
            verbose=False
        )

    @agent
    def accounting_agent(self) -> Agent:
        return Agent(
            **self.agents_config['accounting_agent'],
            verbose=False
        )

    @agent
    def manager_agent(self) -> Agent:
        return Agent(
            **self.agents_config['manager_agent'],
            verbose=False
        )
        
    @task
    def fetch_vehicle_info(self) -> Task:
        return Task(
            **self.tasks_config['fetch_vehicle_info']
        )

    @task
    def analyze_data(self) -> Task:
        return Task(
            **self.tasks_config['analyze_data']
        )

    @task
    def customer_interaction(self) -> Task:
        return Task(
            **self.tasks_config['customer_interaction']
        )

    @task
    def process_payment(self) -> Task:
        return Task(
            **self.tasks_config['process_payment']
        )

    def decide_task(self, user_input: str) -> str:
        """
        Decide which task to delegate based on the user input.

        Args:
            user_input (str): The user's query.

        Returns:
            str: The name of the task to handle the query.
        """
        if "price" in user_input or "cost" in user_input:
            return "analyze_data"
        elif "features" in user_input or "info" in user_input:
            return "fetch_vehicle_info"
        elif "buy" in user_input or "payment" in user_input:
            return "process_payment"
        else:
            return "customer_interaction"
        

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[
                self.researcher_agent(),
                self.analyst_agent(),
                self.sales_agent(),
                self.accounting_agent()
            ],
            tasks=[
                self.fetch_vehicle_info(),
                self.analyze_data(),
                self.customer_interaction(),
                self.process_payment()
            ],
            process=Process.hierarchical,
            manager_agent=self.manager_agent(),
            verbose=True,
            memory=True,
        )
        
