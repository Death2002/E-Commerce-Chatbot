from anthropic import Anthropic
from models import Product

class ChatBot:
    def __init__(self, api_key):
        self.anthropic = Anthropic(api_key=api_key)

    def process_message(self, message):
        message = message.lower()
        
        # Initialize response variable
        bot_input = ""
    
        if "search" in message or "find" in message:
            query = message.replace("search", "").replace("find", "").strip()
            products = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
            
            if products:
                product_list = "\n".join([f"- {product.name} (${product.price:.2f})" for product in products])
                bot_input = f"The user searched for '{query}', and I found the following products:\n{product_list}"
            else:
                bot_input = f"The user searched for '{query}', but no products were found."
        elif "category" in message:
            query = message.replace("category", "").strip()
            products = Product.query.filter(Product.category.ilike(f"%{query}%")).all()
            
            if products:
                product_list = "\n".join([f"- {product.name} (${product.price:.2f})" for product in products])
                bot_input = f"The user asked about the '{query}' category, and I found these products:\n{product_list}"
            else:
                bot_input = f"The user asked about the '{query}' category, but no products were found."
        else:
            bot_input = f"The user asked: {message}"

        try:
            response = self.anthropic.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1000,
                messages=[
                    {"role": "assistant", "content": "I am a helpful e-commerce assistant."},
                    {"role": "user", "content": message},
                    {"role": "assistant", "content": bot_input}
                ]
            )
            return response.content[0].text
        except Exception as e:
            print(e)
            return "Sorry, I encountered an error while processing your request. Please try again later."
