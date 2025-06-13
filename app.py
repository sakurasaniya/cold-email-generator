
---

### 🐍 `app.py`

```python
import gradio as gr

def generate_cold_email(company_name, product_description, recipient_name):
    subject = f"AI Solutions from {company_name} for Your Business"
    email_body = f"""
Subject: {subject}

Dear {recipient_name},

I hope you're doing well. I’m reaching out from {company_name} to introduce our AI-powered solutions tailored to your needs.

Our offerings — {product_description} — can significantly streamline operations, cut costs, and enhance performance. We specialize in solutions that adapt across industries, including supply chain, healthcare, and finance.

We’d love to schedule a brief demo to explore how we can add value to your work.

Best regards,  
[Your Name]  
{company_name}  
[Your Contact Information]
"""
    return email_body.strip()

iface = gr.Interface(
    fn=generate_cold_email,
    inputs=[
        gr.Textbox(label="Your Company Name", placeholder="e.g. MistralX AI"),
        gr.Textbox(label="Product Description", placeholder="e.g. demand forecasting, route optimization, etc."),
        gr.Textbox(label="Recipient's Name", placeholder="e.g. Ankit Verma")
    ],
    outputs=gr.Textbox(label="Generated Cold Email"),
    title="Cold Email Generator",
    description="Enter your company, product, and recipient to generate a professional cold email."
)

iface.launch(share=True)
