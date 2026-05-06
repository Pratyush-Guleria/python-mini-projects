# =================================================================
# MODULE: OBJECT-ORIENTED PROGRAMMING (OOPs)
# CONCEPT: MULTIPLE INHERITANCE & FILE I/O 
# ARCHITECTURE: HYBRID LOGGER (FileWriter + ConsoleNotifier)
# STRATEGY: COMBINING INDEPENDENT FUNCTIONALITIES INTO ONE TOOL
# =================================================================

class FileWriter:
    """
    Handles permanent data storage on the physical hard drive.
    """
    def write_to_file(self, content: str) -> None:
        # 'a' mode means 'Append' - it adds data without deleting old logs 📝
        with open("my_logs.txt", "a") as f:
            f.write(content + "\n")
        print("System: Data successfully committed to disk. ✅")


class ConsoleNotifier:
    """
    Handles real-time terminal notifications.
    """
    def notify(self, message: str) -> None:
        # Professional formatting for terminal output 🔔
        print(f"[NOTIFICATION]: {message}")


class SmartLogger(FileWriter, ConsoleNotifier):
    """
    A Hybrid Class inheriting powers from both File and Console units.
    Demonstrates Multiple Inheritance: (FileWriter, ConsoleNotifier)
    """
    pass  # No extra code needed, it inherits EVERYTHING! 🧬🔥


# =================================
# EXECUTION: 
#==================================

if __name__ == "__main__":
    # 1. Instantiate the Hybrid Tool
    logger = SmartLogger()

    print("--- Initiating System Audit ---")

    # 2. Use Method 1: Console Notification (From ConsoleNotifier)
    logger.notify("I am just testing this")

    # 3. Use Method 2: Permanent Logging (From FileWriter)
    # This will create or update 'my_logs.txt' in your folder. 📂
    logger.write_to_file("Status: Execution Successful. State: HARD. 🦍")

    print("\n[SUCCESS] Check your folder for 'my_logs.txt' to see the legacy! 🟢👊")
