# CUSTOMER SERVICE CHATBOT
# Google Colab - Single Cell

print("====================================")
print("      CUSTOMER SERVICE CHATBOT")
print("====================================")
print("Type 'bye' to end the conversation.\n")

while True:

    user = input("Customer: ").lower().strip()

    if user == "bye":
        print("Support: Thank you for contacting us. Have a nice day!")
        break

    elif "hello" in user or "hi" in user:
        print("Support: Hello! Welcome to our customer service. How can I help you?")

    elif "order" in user and ("status" in user or "track" in user):
        print("Support: Please provide your order ID to check your order status.")

    elif "cancel" in user and "order" in user:
        print("Support: Your order cancellation request has been received.")

    elif "return" in user:
        print("Support: You can return the product within 7 days of delivery.")

    elif "refund" in user:
        print("Support: Refunds are processed within 5-7 business days after approval.")

    elif "payment" in user:
        print("Support: We accept UPI, credit cards, debit cards and net banking.")

    elif "delivery" in user:
        print("Support: Standard delivery usually takes 3-5 business days.")

    elif "complaint" in user or "problem" in user:
        print("Support: We are sorry for the inconvenience. Please describe your problem.")

    elif "thank" in user:
        print("Support: You're welcome! We are happy to help.")

    else:
        print("Support: Sorry, I couldn't understand your request. Please contact our support team.")

print("\nCustomer service session ended.")