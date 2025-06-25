
# chatbot.py
import datetime

financial_data = {
    "Total Revenue": "Microsoft: $211.91B, Tesla: $96.77B, Apple: $383.29B",
    "Net Income Change": "Microsoft: +12.75%, Tesla: -23.65%, Apple: +2.91%",
    "Total Assets": "Microsoft: $448.13B, Tesla: $93.68B, Apple: $352.58B",
    "Cash Flow": "Microsoft: $87.6B, Tesla: $13.89B, Apple: $110.54B",
    "Liabilities": "Microsoft: $222.44B, Tesla: $50.9B, Apple: $290.44B"
}

# Chatbot logic
def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return f"The total revenue is:\n{financial_data['Total Revenue']}"
    elif user_query == "How has net income changed over the last year?":
        return f"The net income change over the last year:\n{financial_data['Net Income Change']}"
    elif user_query == "What are the total assets?":
        return f"Total assets:\n{financial_data['Total Assets']}"
    elif user_query == "What is the cash flow from operations?":
        return f"Cash flow from operating activities:\n{financial_data['Cash Flow']}"
    elif user_query == "What are the total liabilities?":
        return f"Total liabilities:\n{financial_data['Liabilities']}"
    else:
        return "Sorry, I can only provide information on predefined queries."

# Command-line interaction
if __name__ == "__main__":
    print("📊 Welcome to the Financial Chatbot Prototype!")
    print("Type your query (or 'exit' to quit):\n")
    print("Try: What is the total revenue? | How has net income changed over the last year?\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("👋 Goodbye!")
            break
        response = simple_chatbot(user_input)
        print("Bot:", response)
