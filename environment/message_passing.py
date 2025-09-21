from collections import defaultdict
from loguru import logger

class MessageHandler:
    # acts as a mailbox - each agent has separate read and unread message queues.
    # Other agents post messages to the unread queue.
    def __init__(self):
        self.unread_messages = defaultdict(list)  # Queue for unread messages
        self.read_messages = defaultdict(list)    # Queue for read messages

    def post_message(self, message: str, agent_id: str):
        """Post a message to an agent's unread queue."""
        self.unread_messages[agent_id].append(message)
        logger.debug(f"Posted message to {agent_id}: {message}")

    def get_latest_unread_message(self, agent_id: str) -> str|None:
        """Get the latest unread message for an agent."""
        if not self.unread_messages[agent_id]:
            return None
        return self.unread_messages[agent_id][-1]

    def get_all_unread_messages(self, agent_id: str) -> list[str]:
        """Get all unread messages for an agent."""
        return self.unread_messages[agent_id].copy()

    def get_all_read_messages(self, agent_id: str) -> list[str]:
        """Get all read messages for an agent."""
        return self.read_messages[agent_id].copy()

    def mark_message_as_read(self, agent_id: str, message: str) -> bool:
        """Move a specific message from unread to read queue."""
        if message in self.unread_messages[agent_id]:
            self.unread_messages[agent_id].remove(message)
            self.read_messages[agent_id].append(message)
            logger.debug(f"Marked message as read for {agent_id}: {message}")
            return True
        return False

    def mark_all_as_read(self, agent_id: str) -> int:
        """Move all unread messages to read queue for an agent."""
        count = len(self.unread_messages[agent_id])
        if count > 0:
            self.read_messages[agent_id].extend(self.unread_messages[agent_id])
            self.unread_messages[agent_id].clear()
            logger.debug(f"Marked {count} messages as read for {agent_id}")
        return count

    def get_unread_count(self, agent_id: str) -> int:
        """Get the number of unread messages for an agent."""
        return len(self.unread_messages[agent_id])

    def get_read_count(self, agent_id: str) -> int:
        """Get the number of read messages for an agent."""
        return len(self.read_messages[agent_id])

    def get_agents(self) -> list[str]:
        """Get all agents that have messages (read or unread)."""
        all_agents = set(self.unread_messages.keys()) | set(self.read_messages.keys())
        return list(all_agents)

    def display_messages_exchanged(self):
        """Display all messages for all agents in a readable format."""
        agents = self.get_agents()
        if not agents:
            logger.info("📭 No messages have been exchanged yet.")
            return
            
        logger.info("📬 Message Exchange Summary")
        logger.info("=" * 50)
        
        for agent_id in agents:
            unread_count = self.get_unread_count(agent_id)
            read_count = self.get_read_count(agent_id)
            total_count = unread_count + read_count
            
            # Agent header with counts
            status_icon = "🔴" if unread_count > 0 else "✅"
            logger.info(f"{status_icon} Agent: {agent_id}")
            logger.info(f"   📊 Total: {total_count} messages ({unread_count} unread, {read_count} read)")
            
            # Display unread messages
            if self.unread_messages[agent_id]:
                logger.info("   📥 Unread Messages:")
                for i, message in enumerate(self.unread_messages[agent_id], 1):
                    logger.info(f"      {i}. {message}")
            
            # Display read messages
            if self.read_messages[agent_id]:
                logger.info("   📖 Read Messages:")
                for i, message in enumerate(self.read_messages[agent_id], 1):
                    logger.info(f"      {i}. {message}")
            
            logger.info("-" * 30)