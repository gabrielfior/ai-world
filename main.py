from agents.langchain_agent import LangchainAgent
from environment.message_passing import MessageHandler
from environment.world import World


def run_simulation():
    # Currently sync, will later be async
    agent1 = LangchainAgent(agent_id="agent1")
    agent2 = LangchainAgent(agent_id="agent2")
    w = World(message_handler=MessageHandler())
    w.register_agents([agent1, agent2])
    w.run(num_steps=1)


if __name__ == "__main__":
    run_simulation()
