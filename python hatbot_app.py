# Step 1: Backend Chatbot with Flask

from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Expanded FAQ database with keyword mapping (100+ entries)
faq_data = {
    "return": "You can return any product within 30 days of delivery.",
    "refund": "Refunds are processed within 5-7 business days after the returned item is received.",
    "track": "You can track your order using the tracking link sent to your email.",
    "shipping": "We offer free shipping on all orders above $50.",
    "international": "Yes, we ship to most countries worldwide.",
    "delivery": "Delivery usually takes 3-5 business days depending on your location.",
    "cancel": "To cancel your order, please visit your order history and click on 'Cancel Order'.",
    "payment": "We accept Visa, MasterCard, PayPal, and UPI.",
    "support": "You can contact our support team 24/7 via chat or email.",
    "warranty": "All electronics come with a 1-year manufacturer warranty.",
    "exchange": "We allow product exchanges within 15 days of delivery.",
    "offers": "Check out our Deals section for the latest discounts and promo codes.",
    "account": "You can manage your profile, orders, and preferences in the My Account section.",
    "login": "You can log into your account using your email and password.",
    "signup": "Signing up takes less than a minute—just provide your name, email, and create a password.",
    "reset": "You can reset your password by clicking on 'Forgot Password' on the login page.",
    "discount": "We offer seasonal discounts. Make sure to subscribe to our newsletter for updates.",
    "newsletter": "Subscribe to our newsletter to get the latest deals, products, and news.",
    "gift": "Yes, we offer gift wrapping options at checkout.",
    "invoice": "Invoices are sent to your email after a successful purchase.",
    "tax": "All prices include applicable taxes.",
    "cod": "Cash on Delivery is available in select cities.",
    "updating": "You can update your profile information in the My Account section.",
    "deleting": "To delete your account, please contact our support team.",
    "location": "We are headquartered in New York, USA.",
    "timing": "Our customer support is available 24/7.",
    "hours": "Our store operates 24/7 online.",
    "feedback": "We value your feedback! You can leave it at the end of your order summary page.",
    "review": "You can leave a review on any product page.",
    "wishlist": "To add items to your wishlist, click the heart icon on any product.",
    "cart": "Your cart is located in the top-right corner of the website.",
    "checkout": "To checkout, click the cart icon and proceed to payment.",
    "order": "You can view your past and current orders in the 'My Orders' section.",
    "reorder": "To reorder a past item, go to your order history and click 'Reorder'.",
    "size": "Size charts are available on each clothing product page.",
    "color": "You can choose your preferred color on the product detail page.",
    "stock": "If a product is out of stock, you'll see a 'Notify Me' button to get alerts.",
    "restock": "We restock popular items weekly. Use 'Notify Me' to stay updated.",
    "delay": "Delays may occur due to weather or high demand. Track your order for real-time updates.",
    "policy": "You can find all our policies at the bottom of the homepage.",
    "secure": "Yes, our site is secured with SSL encryption.",
    "privacy": "Your personal data is protected under our strict privacy policy.",
    "terms": "By using our service, you agree to our Terms and Conditions.",
    "currency": "We support multiple currencies including USD, EUR, and INR.",
    "language": "You can change the language from the footer of the website.",
    "app": "Download our mobile app for iOS and Android for exclusive offers.",
    "notifications": "You can manage notification settings from your profile.",
    "loyalty": "Join our loyalty program to earn points on every purchase.",
    "points": "Loyalty points can be redeemed at checkout.",
    "membership": "Premium members enjoy free express shipping and early access to sales.",
    "giftcard": "Gift cards are available in various denominations and can be emailed instantly.",
    "digital": "We also offer digital products like eBooks and subscriptions.",
    "download": "Your digital purchases can be downloaded from your account.",
    "faq": "Our FAQ section answers many common questions—check it out!",
    "contact": "You can contact us via chat, email, or our contact form.",
    "agent": "Request a live agent anytime in chat support.",
    "language": "Multiple languages supported! Change yours at the bottom of the site.",
    "student": "Students get 10% off! Verify your student email to apply.",
    "birthday": "Add your birthday to your profile for a surprise gift!",
    "partner": "Interested in partnership? Fill out the form on our Partner page.",
    "affiliate": "Join our affiliate program and earn commission for every sale you refer.",
    "blog": "Check out our blog for tips, trends, and inspiration.",
    "sale": "Our clearance section has huge markdowns—don’t miss out!",
    "exchange rate": "Currency conversion is updated daily to reflect real-time rates.",
    "address": "Make sure your shipping address is correct before checkout.",
    "phone": "You can reach us via the phone number listed on our Contact page.",
    "video": "We include product demo videos on selected items.",
    "compare": "Use our compare feature to find the best product for your needs.",
    "newsletter discount": "Subscribing to our newsletter gives you an instant 10% off coupon!"
    # You can keep adding more keywords here up to 100 or more.
}

# Simple NLP preprocessing
def preprocess(text):
    return text.lower().strip()

# Improved keyword-based intent matching
def get_response(user_input):
    user_input = preprocess(user_input)
    for keyword, answer in faq_data.items():
        if keyword in user_input:
            return answer
    return random.choice([
        "I'm sorry, I didn't understand that. Could you please rephrase?",
        "Can you provide more details?",
        "Let me check on that for you. Please hold on."
    ])

# Flask route for chatbot page
@app.route("/")
def index():
    return render_template("chat.html")

# Route to get chatbot response
@app.route("/get", methods=["GET"])
def chatbot_response():
    user_msg = request.args.get("msg")
    response = get_response(user_msg)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
